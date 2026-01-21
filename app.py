import streamlit as st
import os

# File to store students data
FILE_NAME = "students.txt"

# ------------------ FILE HANDLING ------------------
def load_students():
    """Load students from text file"""
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                student_id, name, age, grade, section = line.strip().split('|')
                students.append({
                    'id': student_id,
                    'name': name,
                    'age': age,
                    'grade': grade,
                    'section': section
                })
    return students

def save_students(students):
    """Save students to text file"""
    with open(FILE_NAME, 'w') as file:
        for student in students:
            line = f"{student['id']}|{student['name']}|{student['age']}|{student['grade']}|{student['section']}\n"
            file.write(line)

# ------------------ ID GENERATION ------------------
def generate_student_id():
    """Generate auto-incremented student ID"""
    students = load_students()
    if not students:
        return "1"  
    else:
        last_id = max(int(student['id']) for student in students)
        return str(last_id + 1)

# ------------------ CRUD OPERATIONS ------------------
def add_student(name, age, grade, section):
    """Add a new student with auto-generated ID"""
    students = load_students()
    student_id = generate_student_id()
    students.append({
        'id': student_id,
        'name': name,
        'age': age,
        'grade': grade,
        'section': section
    })
    save_students(students)
    return True, f"Student added successfully! Student ID: {student_id}"

def search_student(student_id):
    students = load_students()
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def update_student(student_id, name, age, grade, section):
    students = load_students()
    for student in students:
        if student['id'] == student_id:
            student['name'] = name
            student['age'] = age
            student['grade'] = grade
            student['section'] = section
            save_students(students)
            return True, "Student updated successfully!"
    return False, "Student not found!"

def delete_student(student_id):
    students = load_students()
    for i, student in enumerate(students):
        if student['id'] == student_id:
            students.pop(i)
            save_students(students)
            return True, "Student deleted successfully!"
    return False, "Student not found!"

# ------------------ STREAMLIT UI ------------------
st.title("🎓 Student Management System (Auto-generated Student ID)")

menu = st.sidebar.selectbox("Menu", [
    "Add New Student",
    "View All Students",
    "Search Student",
    "Update Student",
    "Delete Student",
    "Exit"            
])

# --------- ADD STUDENT ---------
if menu == "Add New Student":
    st.header("Add New Student")
    with st.form("add_student_form"):
        name = st.text_input("Name")
        age = st.text_input("Age")
        grade = st.text_input("Grade (A-F)")
        section = st.text_input("Section")

        submitted = st.form_submit_button("Add Student")
        if submitted:
            if not name.strip():
                st.error("Name cannot be empty!")
            elif not age.isdigit() or int(age) <= 0:
                st.error("Age must be a positive integer!")
            elif not grade.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
                st.error("Grade must be A-F!")
            elif not section.strip():
                st.error("Section cannot be empty!")
            else:
                success, message = add_student(name, age, grade.upper(), section)
                if success:
                    st.success(message)

# --------- VIEW ALL STUDENTS ---------
elif menu == "View All Students":
    st.header("All Students")
    students = load_students()
    if not students:
        st.info("No students in the database.")
    else:
        st.table(students)

# --------- SEARCH STUDENT ---------
elif menu == "Search Student":
    st.header("Search Student by ID")
    student_id = st.text_input("Enter Student ID to search")
    if st.button("Search"):
        if student_id.strip():
            student = search_student(student_id)
            if student:
                st.success("Student found!")
                st.write(f"**ID:** {student['id']}")
                st.write(f"**Name:** {student['name']}")
                st.write(f"**Age:** {student['age']}")
                st.write(f"**Grade:** {student['grade']}")
                st.write(f"**Section:** {student['section']}")
            else:
                st.error("Student not found!")
        else:
            st.error("Please enter a Student ID!")

# --------- UPDATE STUDENT ---------
elif menu == "Update Student":
    st.header("Update Student Details")
    student_id = st.text_input("Enter Student ID to update")
    if student_id:
        student = search_student(student_id)
        if student:
            with st.form("update_form"):
                name = st.text_input("Name", value=student['name'])
                age = st.text_input("Age", value=student['age'])
                grade = st.text_input("Grade", value=student['grade'])
                section = st.text_input("Section", value=student['section'])

                submitted = st.form_submit_button("Update Student")
                if submitted:
                    if not name.strip() or not section.strip():
                        st.error("Name and Section cannot be empty!")
                    elif not age.isdigit() or int(age) <= 0:
                        st.error("Age must be a positive integer!")
                    elif not grade.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
                        st.error("Grade must be A-F!")
                    else:
                        success, message = update_student(student_id, name, age, grade.upper(), section)
                        if success:
                            st.success(message)
        else:
            st.error("Student not found!")

# --------- DELETE STUDENT ---------
elif menu == "Delete Student":
    st.header("Delete Student")
    student_id = st.text_input("Enter Student ID to delete")
    if st.button("Delete Student"):
        if student_id.strip():
            success, message = delete_student(student_id)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.error("Please enter a Student ID!")

# --------- EXIT PROGRAM ---------
elif menu == "Exit":
    st.header("Thank You for Using the Student Management System!")
    st.success("The program has been closed successfully.")
    st.stop()





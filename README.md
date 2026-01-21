# Student_Management_System
🎓 Student Management System (Streamlit)

A file-based Student Management System built using Python and Streamlit that supports full CRUD operations with auto-generated Student IDs.
This project demonstrates core Python concepts, file handling, and interactive UI development using Streamlit.

🚀 Features

 .Add New Students (Auto-generated Student ID)
 
 .View All Students
 
 .Search Student by ID
 
 .Update Student Details
 
 .Delete Student Records

 .Persistent Storage using Text File
 
 .Input validation for age, grade, and empty fields
 
 .Simple & interactive Streamlit interface

🛠️ Tech Stack

Python

Streamlit

File Handling (TXT)

OS Module

🧠 How the System Works

Student data is stored in a text file (students.txt)

Each record is saved using the format:

id | name | age | grade | section

Student ID is auto-generated based on existing records

CRUD operations update the file dynamically

Streamlit provides an interactive UI for all actions

🎯 Validation Rules

Age must be a positive integer

Grade must be between A–F

Name and Section cannot be empty

Student ID must exist for update/delete actions

<img width="1890" height="917" alt="st student" src="https://github.com/user-attachments/assets/a3a63b4a-0c76-49f2-bb0d-a6c7795ab33d" />

💡 Future Enhancements

Replace text file with SQLite / PostgreSQL

Add login authentication

Export student data to CSV / Excel

Add search by name or grade

Deploy on Streamlit Cloud

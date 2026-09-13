# 1st-py-project
Student Data Manager 
===================== 
A command-line application to manage student records with:
- Add a new student
- Search for a student (by ID or name)
- Update an existing student's info
-  Delete a student
- List all students


## Student Management System

## 📌 About the Project

The **Student Management System** is a simple Python-based project used to store and manage student information.

The project uses **Python for the application/backend** and **MySQL for storing the data**. Python connects to MySQL using the `mysql-connector-python` library.

The main purpose of this project is to make student record management simple and to understand how a Python application works with a database.

---

## ✨ Features

1. Add a new student
2. View student records
3. Search for a student
4. Update student details
5. Delete a student
6. Store student data in MySQL
7. Simple user interface
8. Easy database connectivity

---

## 🛠️ Technologies Used

1.  Python
2. MySQL
3. MySQL Connector for Python
4. VS Code
6. Git & GitHub

---

## 📂 Project Structure

text
Student-Management-System
│
├── frontend.py
├── backend.py
├── requirements.txt
└── README.md


Frontend.py → Handles the user interface and user input.

Backend.py → Handles database operations and connects Python with MySQL.

Requirements.txt → Contains the required Python packages.

README.md → Contains information about the project.

---

# 🔄 Workflow

The project works in the following way:

```text
        User
         │
         ▼
     Frontend
         │
         ▼
      Backend
         │
         ▼
 MySQL Connector
         │
         ▼
 MySQL Database
         │
         ▼
   Student Table
```

### Example: Adding a Student

```text
User enters student details
          ↓
Frontend receives the details
          ↓
Backend processes the details
          ↓
SQL INSERT query is executed
          ↓
MySQL stores the student
          ↓
Success message is displayed
```

# 🔧 CRUD Operations

The system mainly performs four database operations:

| Operation  | What it does                      |
| ---------- | --------------------------------- |
| Create | Adds a new student                |
| Read   | Displays/searches student records |
| Update | Changes student information       |
| Delete | Removes a student record          |

These operations are commonly called **CRUD operations**.

---

# 🗄️ Database

The student information is stored in a MySQL database.

A student record can contain information such as:

```text
Student ID
Name
Age
Course
Email
Phone
```

The backend uses a **MySQL connection and cursor** to execute SQL queries.

---

# 📋 Main Functions

The backend provides functions for different student operations, such as:

```text
add_student()
view_students()
search_student()
update_student()
delete_student()
```

Each function performs the required operation on the MySQL database.

---

# 🎯 Project Objective

The main objective of this project is to learn how to:

* Build a simple Python application
* Connect Python with MySQL
* Write SQL queries
* Perform CRUD operations
* Separate frontend and backend code
* Store and retrieve data from a database
* Use Git and GitHub for project management

---

# 🚀 Future Improvements

In the future, this project can be improved by adding:

* Admin login
* Student login
* Attendance management
* Marks and grades
* Student profile
* Better UI
* REST API
* Web-based version
* Cloud database

---

## 👨‍💻 Author

**R Sai Charan Teja**

Computer Science(AI -ML) Student
AT MALLA REDDY COLLEGE OF ENGINEERING HYDERABAD
BTECH - 2nd YEAR

---

## ⭐ Conclusion

This project is a basic **Student Management System** that demonstrates how a Python application can connect with a MySQL database and perform different operations on student records.

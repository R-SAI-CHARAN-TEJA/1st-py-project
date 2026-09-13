"""
Student Data Manager
=====================
A command-line application to manage student records with:
  - Add a new student
  - Search for a student (by ID or name)
  - Update an existing student's info
  - Delete a student
  - List all students
All data is persisted to a local JSON file (students.json).
"""

import json
import os

DATA_FILE = "students.json"

# DAta handling
def load_data():
    """Load student records from the JSON file. Returns a dict keyed by ID."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: could not read {DATA_FILE} ({e}). Starting with empty data.")
        return {}
def save_data(data):
    """Save the student records dict to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ----------------------------- Core Operations ---------------------------- #

def add_student(data):
    student_id = input("Enter student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in data:
        print(f"A student with ID '{student_id}' already exists.")
        return

    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    grade = input("Enter grade/class: ").strip()
    email = input("Enter email: ").strip()

    data[student_id] = {
        "name": name,
        "age": age,
        "grade": grade,
        "email": email
    }
    save_data(data)
    print(f"Student '{name}' (ID: {student_id}) added successfully.")

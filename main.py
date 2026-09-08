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
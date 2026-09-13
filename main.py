import backend


# ============================================================
# DISPLAY ONE STUDENT
# ============================================================

def print_student(student):

    print("-" * 40)

    print(f"ID:    {student[0]}")
    print(f"Name:  {student[1]}")
    print(f"Age:   {student[2]}")
    print(f"Grade: {student[3]}")
    print(f"Email: {student[4]}")


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    age = input("Enter age: ").strip()

    # Convert age from text to integer
    try:
        age = int(age)
    except ValueError:
        print("Age must be a number.")
        return

    grade = input("Enter grade/class: ").strip()
    email = input("Enter email: ").strip()

    backend.add_student(
        student_id,
        name,
        age,
        grade,
        email
    )


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():

    query = input("Search by ID or name: ").strip()

    if not query:
        print("Search value cannot be empty.")
        return

    results = backend.search_student(query)

    if not results:

        print("No matching student found.")
        return

    print(f"\nFound {len(results)} student(s):")

    for student in results:
        print_student(student)


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():

    student_id = input("Enter student ID to update: ").strip()

    # First search for the student
    results = backend.search_student(student_id)

    if not results:

        print("Student not found.")
        return

    student = results[0]

    print("\nCurrent information:")
    print_student(student)

    print("\nEnter new information:")

    name = input(f"Name [{student[1]}]: ").strip()

    age = input(f"Age [{student[2]}]: ").strip()

    grade = input(f"Grade [{student[3]}]: ").strip()

    email = input(f"Email [{student[4]}]: ").strip()

    # If user leaves something blank,
    # keep the old value.
    if not name:
        name = student[1]

    if not age:
        age = student[2]
    else:
        try:
            age = int(age)
        except ValueError:
            print("Age must be a number.")
            return

    if not grade:
        grade = student[3]

    if not email:
        email = student[4]

    backend.update_student(
        student_id,
        name,
        age,
        grade,
        email
    )

# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():

    student_id = input("Enter student ID to delete: ").strip()

    # Find student first
    results = backend.search_student(student_id)

    if not results:

        print("Student not found.")
        return

    student = results[0]

    print_student(student)

    confirm = input(
        "Are you sure you want to delete this student? (y/n): "
    ).strip().lower()

    if confirm == "y":

        backend.delete_student(student_id)

    else:

        print("Deletion cancelled.")


# ============================================================
# LIST ALL STUDENTS
# ============================================================

def list_students():

    students = backend.get_all_students()

    if not students:

        print("No students found.")
        return

    print(f"\nAll Students ({len(students)} total)")

    for student in students:

        print_student(student)


# ============================================================
# MENU
# ============================================================

MENU = """
========== Student Data Manager ==========

1. Add student
2. Search student
3. Update student
4. Delete student
5. List all students
6. Exit

===========================================
"""


def main():

    while True:

        print(MENU)

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            search_student()

        elif choice == "3":

            update_student()

        elif choice == "4":

            delete_student()

        elif choice == "5":

            list_students()

        elif choice == "6":

            print("Goodbye!")
            break

        else:

            print("Invalid choice. Please select 1-6.")


# Start the program
if __name__ == "__main__":
    main()
import mysql.connector
from mysql.connector import Error


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    """
    Connect Python to MySQL database.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Charan",
            database="student_db"
        )

        return connection

    except Error as e:
        print("Database connection error:", e)
        return None
# ============================================================
# ADD STUDENT
# ============================================================

def add_student(student_id, name, age, grade, email):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:

        # SQL query to insert a new student
        sql = """
        INSERT INTO students
        (student_id, name, age, grade, email)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Values are passed separately.
        # This is safer than directly joining strings into SQL.
        values = (student_id, name, age, grade, email)

        cursor.execute(sql, values)

        # Save the changes permanently
        connection.commit()

        print(f"Student '{name}' added successfully.")
        return True

    except Error as e:

        print("Error adding student:", e)
        return False

    finally:

        # Always close cursor and database connection
        cursor.close()
        connection.close()

# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student(query):

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    try:

        # Search by student ID OR name
        sql = """
        SELECT student_id, name, age, grade, email
        FROM students
        WHERE student_id = %s
           OR name LIKE %s
        """

        values = (query, "%" + query + "%")

        cursor.execute(sql, values)

        # fetchall() gets all matching records
        results = cursor.fetchall()

        return results

    except Error as e:

        print("Error searching student:", e)
        return []

    finally:

        cursor.close()
        connection.close()

#=============================================================
# GET ALL STUDENT
# ============================================================

def get_all_students():

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    try:
        # Get all students
        sql = """
        SELECT student_id, name, age, grade, email
        FROM students
        ORDER BY student_id
        """

        cursor.execute(sql)

        # Get all records
        students = cursor.fetchall()

        return students

    except Error as e:
        print("Error getting students:", e)
        return []

    finally:
        cursor.close()
        connection.close()

# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student(student_id, name, age, grade, email):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:

        sql = """
        UPDATE students
        SET name = %s,
            age = %s,
            grade = %s,
            email = %s
        WHERE student_id = %s
        """

        values = (name, age, grade, email, student_id)

        cursor.execute(sql, values)

        # rowcount tells us how many records were changed
        if cursor.rowcount == 0:

            print("No student found with this ID.")
            return False

        connection.commit()

        print("Student updated successfully.")
        return True

    except Error as e:

        print("Error updating student:", e)
        return False

    finally:

        cursor.close()
        connection.close()

# ============================================================
# UPDATE STUDENT
# ============================================================

def delete_student(query):
    """
    Delete a student using Student ID OR Student Name.
    """

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        # Delete using ID OR Name
        sql = """
        DELETE FROM students
        WHERE student_id = %s
           OR name = %s
        """

        # Same search value is checked against both columns
        values = (query, query)

        cursor.execute(sql, values)

        # Check if anything was deleted
        if cursor.rowcount == 0:
            print("No student found with that ID or name.")
            return False

        # Save the DELETE operation
        connection.commit()

        print("Student deleted successfully.")
        return True

    except Error as e:
        print("Error deleting student:", e)
        return False

    finally:
        cursor.close()
        connection.close()

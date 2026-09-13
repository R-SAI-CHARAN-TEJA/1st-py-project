import mysql.connector
from mysql.connector import Error


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    """
    Connect Python to MySQL database.
    Change the password to your MySQL password.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_MYSQL_PASSWORD",
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

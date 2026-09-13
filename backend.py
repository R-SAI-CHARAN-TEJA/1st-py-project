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

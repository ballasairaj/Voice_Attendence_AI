import sqlite3

from datetime import datetime


def get_connection():

    conn = sqlite3.connect(
        "database/attendance.db"
    )

    return conn


def create_attendance_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_name TEXT,

        status TEXT,

        date TEXT,

        time TEXT
    )
    """)

    conn.commit()

    conn.close()

    print("Attendance table ready")


def already_marked(student_name):

    conn = get_connection()

    cursor = conn.cursor()

    today_date = datetime.now().strftime(
        "%Y-%m-%d"
    )

    cursor.execute("""
    SELECT *
    FROM attendance
    WHERE student_name = ?
    AND date = ?
    """, (
        student_name,
        today_date
    ))

    result = cursor.fetchone()

    conn.close()

    return result is not None


def mark_attendance(
        student_name,
        status
):

    if already_marked(student_name):

        print(
            f"{student_name} already processed today"
        )

        return

    conn = get_connection()

    cursor = conn.cursor()

    current_date = datetime.now().strftime(
        "%Y-%m-%d"
    )

    current_time = datetime.now().strftime(
        "%H:%M:%S"
    )

    cursor.execute("""
    INSERT INTO attendance (

        student_name,

        status,

        date,

        time

    )

    VALUES (?, ?, ?, ?)
    """, (

        student_name,

        status,

        current_date,

        current_time
    ))

    conn.commit()

    conn.close()

    print(
        f"{student_name} marked {status}"
    )



# import sqlite3

# from datetime import datetime


# # Function to create database connection
# def get_connection():

#     conn = sqlite3.connect("database/attendance.db")

#     return conn


# # Function to create attendance table
# def create_attendance_table():

#     conn = get_connection()

#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS attendance (

#         id INTEGER PRIMARY KEY AUTOINCREMENT,

#         student_name TEXT,

#         status TEXT,

#         date TEXT,

#         time TEXT
#     )
#     """)

#     conn.commit()

#     conn.close()

#     print("Attendance table ready")


# # Function to check duplicate attendance
# def already_marked(student_name):

#     conn = get_connection()

#     cursor = conn.cursor()

#     today_date = datetime.now().strftime("%Y-%m-%d")

#     cursor.execute("""
#     SELECT * FROM attendance
#     WHERE student_name = ?
#     AND date = ?
#     """, (student_name, today_date))

#     result = cursor.fetchone()

#     conn.close()

#     return result is not None


# # Function to mark attendance
# def mark_attendance(student_name):

#     # Prevent duplicate attendance
#     if already_marked(student_name):

#         print(f"{student_name} already marked present today")

#         return

#     conn = get_connection()

#     cursor = conn.cursor()

#     current_date = datetime.now().strftime("%Y-%m-%d")

#     current_time = datetime.now().strftime("%H:%M:%S")

#     cursor.execute("""
#     INSERT INTO attendance (
#         student_name,
#         status,
#         date,
#         time
#     )
#     VALUES (?, ?, ?, ?)
#     """, (
#         student_name,
#         "Present",
#         current_date,
#         current_time
#     ))

#     conn.commit()

#     conn.close()

#     print(f"{student_name} marked PRESENT")
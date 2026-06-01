import sqlite3

# Create database connection
conn = sqlite3.connect("database/attendance.db")

cursor = conn.cursor()

# Create attendance table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    status TEXT
)
""")

conn.commit()

# Function to mark attendance
def mark_attendance(student_name):

    cursor.execute("""
    INSERT INTO attendance(student_name, status)
    VALUES (?, ?)
    """, (student_name, "Present"))

    conn.commit()

    print(f"{student_name} marked PRESENT")
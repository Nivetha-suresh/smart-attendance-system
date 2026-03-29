import sqlite3


def create_tables():
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()

    # Students table → one student = one row
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            image_path TEXT
        )
    ''')

    # Attendance table
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            date TEXT,
            time TEXT,
            status TEXT
        )
    ''')

    conn.commit()
    conn.close()


# ---------------- INSERT STUDENT ----------------
def insert_student(name, image_path):
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()

    # Check if student already exists
    c.execute("SELECT * FROM students WHERE name=?", (name,))
    existing = c.fetchone()

    if not existing:
        c.execute(
            "INSERT INTO students (name, image_path) VALUES (?, ?)",
            (name, image_path)
        )

    conn.commit()
    conn.close()


# ---------------- MARK ATTENDANCE ----------------
def mark_attendance(name, date, time):
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()

    # Prevent duplicate attendance for same day
    c.execute(
        "SELECT * FROM attendance WHERE name=? AND date=?",
        (name, date)
    )

    existing = c.fetchone()

    if not existing:
        c.execute(
            "INSERT INTO attendance (name, date, time, status) VALUES (?, ?, ?, ?)",
            (name, date, time, "Present")
        )

    conn.commit()
    conn.close()


# ---------------- GET ATTENDANCE ----------------
def get_attendance():
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()

    c.execute("SELECT * FROM attendance ORDER BY date DESC, time DESC")
    data = c.fetchall()

    conn.close()
    return data


# ---------------- GET STUDENTS ----------------
def get_students():
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()

    c.execute("SELECT * FROM students")
    data = c.fetchall()

    conn.close()
    return data

#clear_db.py
# import sqlite3

# def clear_database():
#     conn = sqlite3.connect("attendance.db")
#     c = conn.cursor()

#     # Delete all student data
#     c.execute("DELETE FROM students")

#     # Delete all attendance data
#     c.execute("DELETE FROM attendance")

#     # Reset auto increment IDs
#     c.execute("DELETE FROM sqlite_sequence WHERE name='students'")
#     c.execute("DELETE FROM sqlite_sequence WHERE name='attendance'")

#     conn.commit()
#     conn.close()
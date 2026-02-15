from db import connect


def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        mark INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()


def add_student(name, mark):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, mark) VALUES (?, ?)",
        (name, mark)
    )
    conn.commit()
    conn.close()


def get_students():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_student(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cur.fetchone()
    conn.close()
    return row


def update_student(student_id, name, mark):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET name = ?, mark = ? WHERE id = ?",
        (name, mark, student_id)
    )
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()

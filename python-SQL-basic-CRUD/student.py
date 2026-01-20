from db import get_connection

#add students
def add_student(name, email, age, department):
    conn = get_connection()
    cur = conn.cursor()

    query = """INSERT INTO students (name, email, age, department)
    VALUES (%s, %s, %s, %s);"""
    cur.execute(query, (name, email, age, department))

    conn.commit()
    cur.close()
    conn.close()

#view students
def get_all_students():
    conn= get_connection()
    cur = conn.cursor()

    query = """SELECT * FROM students;"""
    cur.execute(query)
    students = cur.fetchall()

    cur.close()
    conn.close()
    return students

#delete student
def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()

    query = """DELETE FROM students WHERE id = %s;"""
    cur.execute(query, (student_id,))

    conn.commit()
    cur.close()
    conn.close()

#update student data
def update_student(student_id, department, email):
    conn = get_connection()
    cur = conn.cursor()

    query = """UPDATE students SET department = %s, SET email = %s WHERE id = %s;"""
    cur.execute(query, (department, email, student_id))

    conn.commit()
    cur.close()
    conn.close()
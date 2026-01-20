import psycopg2

def get_connection():
    return psycopg2.connect(
        database="student_db",
        host="localhost",
        user="postgres",
        password="123",
        port="5432"
    ) 
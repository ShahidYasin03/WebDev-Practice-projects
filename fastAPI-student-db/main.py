import students
import json
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()

with open('F:\\Python\\fastAPI-student-db\\config.json', 'r') as file:
    config = json.load(file)

db_table = config['postgres'].get('db_table')

class st(BaseModel):
    name: str
    email: str
    age: int
    department: str

@app.get("/")
def root():
    return {"Message": "Welcome home."}

@app.get("/students/{id}")
def get_students(id: int):
    query = f"""SELECT * FROM {db_table} WHERE id = %s"""
    params = (id,)
    data = students.read_db(query, params)
    
    if data:
        return data[0]
    else:
        return Response(content="Not found", status_code=status.HTTP_404_NOT_FOUND)

@app.get("/students")
def get_students():
    query = f"""SELECT * FROM {db_table};"""
    data = students.read_db(query)
    if data:
        return {"Data": data}
    else:
        return {"Data": "Not found"}

@app.post("/students")
def create_student(student: st):
    query = f"""
        INSERT INTO {db_table} (name, email, age, department)
        VALUES (%s, %s, %s, %s) RETURNING *;
    """
    params = (student.name, student.email, student.age, student.department)
    data = students.write_db(query, params)
    return {"Message": "Student added", "Data": data}

@app.put("/students/{id}")
def update_student(student: st, id: int):
    query = f"""UPDATE {db_table} SET name = %s, email = %s, age = %s, department = %s WHERE id = %s RETURNING *;"""

    params = (student.name, student.email, student.age, student.department, id)

    data = students.update_db(query, params)
    return {"Message": data}

@app.delete("/students/{id}")
def delete_student(id: int):
    query = f"""DELETE FROM {db_table} WHERE id = %s RETURNING id"""
    params = (id,)

    deleted = students.delete_db(query, params)
    if deleted:
        return {"Message": "Successfully deleted"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {id} not found"
        )
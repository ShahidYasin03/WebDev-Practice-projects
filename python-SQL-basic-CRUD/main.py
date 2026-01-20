import student

#menu
def show_menu():
    print("""
    ===== Student Manager =====
    1. Add student
    2. View students
    3. Update student
    4. Delete student
    5. Exit
    """)
 
#print student data
def print_students_table(students):
    print("-" * 72)
    print(f"{'ID':<5} {'Name':<15} {'Email':<25} {'Age':<5} {'Dept':<10}")
    print("-" * 72)

    for s in students:
        print(f"{s[0]:<5} {s[1]:<15} {s[2]:<25} {s[3]:<5} {s[4]:<10}")

    print("-" * 72)
 
#add student 
def add_Data():
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    try:
        student.add_student(name, email, age, department)
        print("Student added to Database successfully!")
    except Exception:
        print("Couldn't Add data!")

#update student department
def update():
    student_id = int(input("Enter student ID: "))
    department = input("Enter new department: ")
    email = input("Enter new email: ")
    try:
        student.update_student(student_id, department, email)
        print("Data updated successfully!")
    except Exception:
        print("Couldn't update student data!")

#delete student data
def delete():
    student_id = int(input("Enter student ID: "))
    try:
        student.delete_student(student_id)
        print("Student data deleted!")
    except Exception:
        print("Couldn't Delete Data!")

#main
def main():
    while True:
        show_menu()
        choice = input("choose option: ")
        match choice:
            case "1":
                add_Data()
            case "2":
                students = student.get_all_students()
                print_students_table(students)
            case "3":
                update()
            case "4":
                delete()
            case "5":
                print("Program closed!!!")
                break
            case _:
                print("invalid option!")

if __name__ == "__main__":
    main()
    print("-"*100)
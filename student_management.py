import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rukmini@2005",
    database="student_management"
)

cursor = conn.cursor()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Insert Student")
    print("2. View Students")
    print("3. Update Student by ID")
    print("4. Delete Student by ID")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, course))
        conn.commit()
        print("Student Inserted Successfully")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        print("\nStudent Records:")
        for row in rows:
            print(row)

    elif choice == "3":
        student_id = int(input("Enter ID to Update: "))
        new_course = input("Enter New Course: ")

        sql = "UPDATE students SET course=%s WHERE id=%s"
        cursor.execute(sql, (new_course, student_id))
        conn.commit()
        print("Student Updated Successfully")

    elif choice == "4":
        student_id = int(input("Enter ID to Delete: "))

        sql = "DELETE FROM students WHERE id=%s"
        cursor.execute(sql, (student_id,))
        conn.commit()
        print("Student Deleted Successfully")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")

conn.close()
print("Program Ended")
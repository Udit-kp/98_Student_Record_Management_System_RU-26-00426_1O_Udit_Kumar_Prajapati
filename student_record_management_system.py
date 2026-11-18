

students = []

HEADERS = ("Roll No.", "Name", "Course", "Marks")

def add_student():
    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:
            if student["roll"] == roll:
                print(f"Roll number {roll} already exists.")
                return

        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))

    
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        
        student = {
            "roll": roll,
            "name": name,
            "course": course,
            "marks": marks
        }

        students.append(student)

        print(f"Record added: {roll} | {name} | {course} | {marks}")

    except ValueError:
        print("Invalid input. Please enter numbers correctly.")



def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n" + "-" * 55)
    print(f"{HEADERS[0]:<12}{HEADERS[1]:<15}{HEADERS[2]:<15}{HEADERS[3]}")
    print("-" * 55)

    for student in students:
        print(
            f"{student['roll']:<12}"
            f"{student['name']:<15}"
            f"{student['course']:<15}"
            f"{student['marks']}"
        )

    print("-" * 55)



def search_student():
    try:
        roll = int(input("Enter Roll Number to Search: "))

        for student in students:
            if student["roll"] == roll:
                print(
                    f"{student['roll']} | {student['name']} | "
                    f"{student['course']} | {student['marks']}"
                )
                return

        print(f"Roll number {roll} not found.")

    except ValueError:
        print("Invalid roll number.")



def update_marks():
    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:
            if student["roll"] == roll:
                marks = int(input("Enter New Marks: "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                    return

                student["marks"] = marks
                print(f"Marks updated: {marks}")
                return

        print(f"Roll number {roll} not found.")

    except ValueError:
        print("Invalid input.")



def delete_student():
    try:
        roll = int(input("Enter Roll Number to Delete: "))

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print(f"Record deleted: {roll}")
                return

        print(f"Roll number {roll} not found.")

    except ValueError:
        print("Invalid roll number.")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Record Management System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")



if __name__ == "__main__":
    main()
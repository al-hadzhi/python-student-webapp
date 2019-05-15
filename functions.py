students = []


def get_students_titlecase():
    """
    Returns an object containing the students titlecase.

    :return:
    """
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    """
    Prints the students titlecase.

    :return:
    """
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=322):
    """
    Adds a a new student with the corresponding Name and ID.

    :param name: Name of the student.
    :param student_id: Optional information with the student ID.
    :return:
    """
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    """
    Writes a new student in the students.txt file.

    :param student:
        The student to be written in the file.
    :return:
    """
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("File couldn't be saved.")


def read_file():
    """
    Reads every individual line from the students.txt file and adds it to the students.

    :return:
    """
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
    except Exception:
        print("File couldn't be read.")


read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)



"""while True:
    usr_prompt = input("Would you like to add a student to the list? [Y/N]: ").capitalize()
    if usr_prompt != "Y" and usr_prompt != "N":
        print("Invalid input, please provide correct input.")
        continue
    elif usr_prompt == "Y":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_student(student_name, student_id)
        print_students_titlecase()
    elif usr_prompt == "N":
        break
"""
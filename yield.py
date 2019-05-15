students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            students.append(student)
        f.close()
    except Exception:
        print("File couldn't be read.")


read_file()
print(students)
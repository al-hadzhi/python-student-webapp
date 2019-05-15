print("Hello World")


"""Lists"""

student_names = ["Mark", "Katerina", "Jessica", "Sally", "George", "Peter", "Alan", "Charles"]
student_names[-3] = "James"

student_names.append("Homer")

if "James" in student_names and len(student_names) == 4:
    print("James is in the list so Ashley has to come as well.")
    student_names.append("Ashley")

for name in student_names:
    if name == "Sally":
        print("Sally was found!")
        continue
    elif name == "Charles":
        continue
    print("Currently testing " + name)


""""Dictionaries"""

student = {
    "first_name": "Mark",
    "student_id": 15163,
    "feedback": None
}

print(format(student["first_name"]))
print(student.get("last_name", "Last name not available!"))

print(student.keys())
student["last_name"] = "Bond"

try:
    last_name = student["middle_name"]
except KeyError as error:
    print("Error! Middle name not found!")
    print(error)

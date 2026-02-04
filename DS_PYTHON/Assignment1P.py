#question 1
# def list_operations():
#     lst=[23,33,44,55,11]
#     print(f"Original list : {lst}")
#     lst.append(25)
#     print(f"After adding 25 : {lst}")
#     lst.insert(2,22)
#     print(f"After adding 22 at index 2 : {lst}")
#     l2=[100,200,300]
#     lst.extend(l2)
#     print(f"After extending l2[100,200,300] : {lst}")
#     lst.pop(1)
#     print(f"After popping out element at index 1 : {lst}")
#     lst.remove(55)
#     print(f"After removing 55 : {lst}")
#     x=11
#     ans=11 in lst
#     print(f"Is 11 is present in list? : {ans}")

# def set_operations():
#     s = {23, 33, 44, 55, 11}
#     print(f"Original set : {s}")
#     s.add(25)
#     print(f"After adding 25 : {s}")
#     s.remove(33)
#     print(f"After removing 33 : {s}")
#     x = 44
#     ans = x in s
#     print(f"Is {x} present in set? : {ans}")
#     print("Traversal of set:", end=" ")
#     for item in s:
#         print(item, end=" ")
#     print("\n")

# def tuple_operations():
#     t = (23, 33, 44, 55, 11)
#     print(f"Original tuple : {t}")
#     x = 44
#     ans = x in t
#     print(f"Is {x} present in tuple? : {ans}")
#     print("Traversal of tuple:", end=" ")
#     for item in t:
#         print(item, end=" ")
#     print("\n")

# def dict_operations():
#     d = {"name": "John", "age": 30, "city": "New York"}
#     print(f"Original dictionary : {d}")
#     d["job"] = "Engineer"
#     print(f"After adding job : {d}")
#     del d["city"]
#     print(f"After removing 'city' : {d}")
#     d["age"] = 31
#     print(f"After updating age : {d}")
#     key = "name"
#     ans = key in d
#     print(f"Is '{key}' present in dictionary? : {ans}")
#     print("Traversal of dictionary:")
#     for key, value in d.items():
#         print(f"{key}: {value}", end=" ")
#     print("\n")

# def string_operations():
#     s = "Hello, Python!"
#     print(f"Original string : {s}")
#     new_string = s.replace("Python", "World")
#     print(f"After updating string : {new_string}")
#     substring = "Python"
#     ans = substring in s
#     print(f"Is '{substring}' present in string? : {ans}")
#     print("Traversal of string:", end=" ")
#     for char in s:
#         print(char, end=" ")
#     print("\n")


# list_operations()
# set_operations()
# tuple_operations()
# dict_operations()
# string_operations()

#question 2
# student_db = []

# def add_student():
#     name = input("Enter student's name: ")
#     age = int(input("Enter student's age: "))
#     grade = input("Enter student's grade: ")
#     courses = input("Enter the courses (comma-separated): ").split(",")
#     courses = [course.strip() for course in courses]
    
#     student = {
#         'name': name,
#         'age': age,
#         'grade': grade,
#         'courses': courses
#     }
    
#     student_db.append(student)
#     print(f"{name}'s record added successfully!\n")

# def display_students():
#     if not student_db:
#         print("No students found in the database.\n")
#     else:
#         print("\nStudent Records:")
#         for student in student_db:
#             print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Courses: {', '.join(student['courses'])}")
#         print()

# def search_student():
#     name = input("Enter the name of the student to search for: ")
#     found = False
#     for student in student_db:
#         if student['name'].lower() == name.lower():
#             print(f"\nStudent Found: {student}")
#             found = True
#             break
#     if not found:
#         print(f"No student found with the name {name}.\n")

# def delete_student():
#     name = input("Enter the name of the student to delete: ")
#     found = False
#     for student in student_db:
#         if student['name'].lower() == name.lower():
#             student_db.remove(student)
#             print(f"{name}'s record deleted successfully!\n")
#             found = True
#             break
#     if not found:
#         print(f"No student found with the name {name}.\n")

# while True:
#     print("\nStudent Record Management System")
#     print("1. Add Student")
#     print("2. Display All Students")
#     print("3. Search Student by Name")
#     print("4. Delete Student Record")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':
#         add_student()
#     elif choice == '2':
#         display_students()
#     elif choice == '3':
#         search_student()
#     elif choice == '4':
#         delete_student()
#     elif choice == '5':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

#question 3
def perform_operations():
    print("Arithmetic Operations Program")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    if num2 != 0:
        division = num1 / num2
        modulus = num1 % num2
    else:
        division = "Undefined (cannot divide by zero)"
        modulus = "Undefined (cannot modulus by zero)"
    power = num1 ** num2

    print(f"\nResults:")
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")
    print(f"Modulus: {num1} % {num2} = {modulus}")
    print(f"Power: {num1} ^ {num2} = {power}")

perform_operations()

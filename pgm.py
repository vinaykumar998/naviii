
print("----- Student Admission Form -----")

name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course name: ")
marks = float(input("Enter your marks: "))

print("\n----- Admission Details -----")
print("Student Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)

if marks >= 35:
    print("Admission Status: Eligible for Admission")
else:
    print("Admission Status: Not Eligible for Admission")
    print("Reason: Marks are below the required threshold for admission.")
    
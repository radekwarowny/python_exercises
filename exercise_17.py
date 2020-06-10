# More User Input of Data

print("Please enter the following information so I can sell it for a profit!\n")

firstName = input("First name: ")
lastName = input("Last name: ")
grade = input("Grade (9-12): ")
studentID = input("Student ID: ")
login = input("Login: ")
gpa = input("GPA (0.0-4.0): ")

print()

print("Your information: ")
print("\tLogin:  ", login)
print("\tID:     ", studentID)
print("\tName:    {}, {}".format(lastName, firstName))
print("\tGPA:    ", gpa)
print("\tGrade:  ", grade)

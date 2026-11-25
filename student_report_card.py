students = []

print("===============================")
print("Student Report Card")
print("===============================")    

name = input("Enter student name: ")
admission = input("Enter student admission number: ")
students_class = input("Enter class: ")
maths = float(input("mathematics: "))
English = float(input("English: "))
kiswahili = float(input("Kiswahili: "))
science = float(input("Science: "))
social_studies = float(input("Social Studies: "))

# Calculate total marks and average
total_marks = maths + English + kiswahili + science + social_studies

# Calculate average marks
average_marks = total_marks / 5 

print("\nSTUDENT REPORT CARD")
print("Name:", name)
print("Admission Number:", admission)
print("Class:", students_class)
print("Total marks:", total_marks)
print("Average:", average_marks)

if average_marks >= 80:
    print("Grade: A")
elif average_marks >= 70:
    print("Grade: B")
elif average_marks >= 60:
    print("Grade: C")
elif average_marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")   
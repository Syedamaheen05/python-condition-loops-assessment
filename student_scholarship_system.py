#  STUDENT SCHOLARSHIP SYSTEM

print("==== Student Scholarship System ====")
student_name = input("Enter your name: ")
is_valid = True

# Initialize variables
student_marks = None
student_attendance = None
family_income = None

try:
    student_marks = float(input("Enter your academic marks (%): "))
    student_attendance = float(input("Enter your attendance (%): "))
    family_income = float(input("Enter your family income: "))

except ValueError:
    print("Invalid input! Please enter numeric values.")
    is_valid = False

else:
    # Validate academic marks
    if student_marks < 0 or student_marks > 100:
        print("Invalid marks!")
        is_valid = False
    elif student_marks >= 80:
        print("Eligible academically!")
    else:
        print("Not eligible academically!")

    # Validate attendance
    if student_attendance < 0 or student_attendance > 100:
        print("Invalid attendance percentage!")
        is_valid = False
    elif student_attendance >= 85:
        print("Eligible due to attendance!")
    else:
        print("Not eligible due to attendance!")

    # Validate family income
    if family_income < 0:
        print("Invalid family income!")
        is_valid = False
    elif family_income <= 50000:
        print("Eligible due to income criteria!")
    else:
        print("Not eligible due to income criteria!")

# Overall eligibility
if is_valid:
    if student_marks >= 80 and student_attendance >= 85 and family_income <= 50000:
        if student_marks >= 90:
            print("Scholarship Award: Full Scholarship!")
        else:
            print("Scholarship Award: Partial Scholarship!")

    else:
        print("Student is not eligible for scholarship!")

else:
    print("Please correct the input values and try again.")

# Scholarship Evaluation Report
print("\n=================================")
print("      SCHOLARSHIP EVALUATION REPORT")
print("=================================")

print(f"Student Name: {student_name}")

if student_marks is not None:
    print(f"Academic Marks: {student_marks}%")
else:
    print("Academic Marks: Not available")

if student_attendance is not None:
    print(f"Attendance: {student_attendance}%")
else:
    print("Attendance: Not available")

if family_income is not None:
    print(f"Family Income: Rs. {family_income}")
else:
    print("Family Income: Not available")

print("\nScholarship Status:")

if not is_valid:
    print("Invalid Input")
elif student_marks >= 80 and student_attendance >= 85 and family_income <= 50000:
    print("Eligible")
else:
    print("Not Eligible")

if is_valid:
    if student_marks < 80 or student_attendance < 85 or family_income > 50000:
        print("\nReasons for Ineligibility:")

        if student_marks < 80:
            print("- Academic marks are below 80%.")

        if student_attendance < 85:
            print("- Attendance is below 85%.")

        if family_income > 50000:
            print("- Family income exceeds Rs. 50,000.")
else:
    print("\nReport Status: Cannot evaluate due to invalid inputs.")
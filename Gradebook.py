# Function to determine letter grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Ask for student name
student_name = input("Enter student name: ")

# Ask for 5 grades (no loops)
grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))
grade3 = int(input("Enter grade 3: "))
grade4 = int(input("Enter grade 4: "))
grade5 = int(input("Enter grade 5: "))

# Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5]

# Calculate average
average = sum(grades) / len(grades)

# Get letter grade
letter_grade = get_letter_grade(average)

# Output
print()
print(student_name)
print()
print("Average:", average)
print()
print("Letter Grade:", letter_grade)
# Student Grade Calculator (Docker + Jenkins)

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def print_grade_criteria():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")


# ---------------- MAIN ----------------

# Predefined student details
student = {
    "name": "Sahana",
    "department": "BCA",
    "semester": 3,
    "marks": [90, 90, 90]
}

# Calculate average
average = sum(student["marks"]) / len(student["marks"])

# Assign grade
grade = calculate_grade(average)

# Print grade criteria (KEY LINE)
print_grade_criteria()

# Display student details
print("\n--- Student Details ---")
print("Name:", student["name"])
print("Department:", student["department"])
print("Semester:", student["semester"])

print("\n--- Subject Marks ---")
print("Subject 1:", student["marks"][0])
print("Subject 2:", student["marks"][1])
print("Subject 3:", student["marks"][2])

print("\nAverage Marks:", round(average, 2))
print("Final Grade:", grade)
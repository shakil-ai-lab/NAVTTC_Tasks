def check_number(num):
    """Check if a number is positive, negative, or zero, and if it's even or odd."""
    
    # Check if positive, negative, or zero
    if num > 0:
        print(f"{num} is a positive number")
    elif num < 0:
        print(f"{num} is a negative number")
    else:
        print(f"{num} is zero")
    
    # Check if even or odd
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")


def check_age(age):
    """Check age group and eligibility."""
    
    if age < 13:
        print(f"You are a child (Age: {age})")
    elif age >= 13 and age < 18:
        print(f"You are a teenager (Age: {age})")
    elif age >= 18 and age < 60:
        print(f"You are an adult (Age: {age})")
    else:
        print(f"You are a senior citizen (Age: {age})")


def get_grade(marks):
    """Determine grade based on marks."""
    
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return grade


# Main Program
print("=== Number Classification ===")
num = float(input("Enter a number: "))
check_number(num)

print("\n=== Age Classification ===")
age = int(input("Enter your age: "))
check_age(age)

print("\n=== Grade Calculator ===")
marks = float(input("Enter your marks (0-100): "))
grade = get_grade(marks)
print(f"Your marks: {marks}")
print(f"Your grade: {grade}")

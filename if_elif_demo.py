def get_day_name(day_number):
    """Convert day number (1-7) to day name using if-elif."""
    
    if day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    elif day_number == 7:
        return "Sunday"
    else:
        return "Invalid day number"


def get_season(month):
    """Determine season based on month number using if-elif."""
    
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"


def get_grade_letter(marks):
    """Assign grade letter based on marks using if-elif."""
    
    if marks >= 90:
        return "A (Excellent)"
    elif marks >= 80:
        return "B (Very Good)"
    elif marks >= 70:
        return "C (Good)"
    elif marks >= 60:
        return "D (Pass)"
    elif marks >= 50:
        return "E (Marginal Pass)"
    else:
        return "F (Fail)"


def check_character_type(char):
    """Check if character is digit, vowel, consonant, or special using if-elif."""
    
    if char.isdigit():
        return "Digit"
    elif char.lower() in ['a', 'e', 'i', 'o', 'u']:
        return "Vowel"
    elif char.isalpha():
        return "Consonant"
    elif char.isspace():
        return "Space"
    else:
        return "Special Character"


def calculate_bill(units):
    """Calculate electricity bill based on units using if-elif."""
    
    # Rate: First 100 units - $2/unit, 101-200 - $3/unit, 201-300 - $4/unit, Above 300 - $5/unit
    
    if units <= 100:
        bill = units * 2
        rate = "$2 per unit"
    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)
        rate = "$2 for first 100, $3 for rest"
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 4)
        rate = "$2 + $3 + $4 for rest"
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 4) + ((units - 300) * 5)
        rate = "$2 + $3 + $4 + $5 for rest"
    
    return bill, rate


def get_age_category(age):
    """Categorize person by age using if-elif."""
    
    if age < 5:
        return "Toddler"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 30:
        return "Young Adult"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"


# Main Program
print("=" * 60)
print("IF-ELIF STATEMENT DEMONSTRATIONS")
print("=" * 60)

# Example 1: Day Name
print("\n1. DAY NAME CONVERTER")
print("-" * 60)
for day in [1, 3, 5, 7, 9]:
    print(f"Day {day}: {get_day_name(day)}")

# Example 2: Season Finder
print("\n2. SEASON FINDER")
print("-" * 60)
for month in [1, 4, 7, 10, 12]:
    print(f"Month {month}: {get_season(month)}")

# Example 3: Grade Calculator
print("\n3. GRADE CALCULATOR")
print("-" * 60)
marks_list = [95, 85, 75, 65, 55, 45]
for marks in marks_list:
    print(f"Marks: {marks} → {get_grade_letter(marks)}")

# Example 4: Character Type
print("\n4. CHARACTER TYPE CHECKER")
print("-" * 60)
characters = ['5', 'a', 'b', ' ', '@']
for char in characters:
    print(f"Character '{char}': {check_character_type(char)}")

# Example 5: Electricity Bill Calculator
print("\n5. ELECTRICITY BILL CALCULATOR")
print("-" * 60)
units_list = [50, 150, 250, 350]
for units in units_list:
    bill, rate = calculate_bill(units)
    print(f"Units: {units} → Bill: ${bill} ({rate})")

# Example 6: Age Category
print("\n6. AGE CATEGORY CLASSIFIER")
print("-" * 60)
ages = [3, 10, 15, 25, 45, 65]
for age in ages:
    print(f"Age {age}: {get_age_category(age)}")

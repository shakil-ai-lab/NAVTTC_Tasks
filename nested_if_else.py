def check_student_eligibility(age, gpa):
    """Check student eligibility for scholarship using nested if-else."""
    
    if age >= 18:
        if gpa >= 3.5:
            if age <= 25:
                print(f"Age: {age}, GPA: {gpa}")
                print("✓ Eligible for merit scholarship")
            else:
                print(f"Age: {age}, GPA: {gpa}")
                print("✓ Eligible for graduate scholarship")
        else:
            if gpa >= 3.0:
                print(f"Age: {age}, GPA: {gpa}")
                print("✓ Eligible for general scholarship")
            else:
                print(f"Age: {age}, GPA: {gpa}")
                print("✗ Not eligible for any scholarship")
    else:
        print(f"Age: {age}")
        print("✗ Must be 18 or older to apply")


def traffic_light_action(color):
    """Nested if-else for traffic light system."""
    
    if color == "red":
        print("Traffic Light: RED")
        print("Action: STOP")
    elif color == "yellow":
        print("Traffic Light: YELLOW")
        if color == "yellow":
            print("Action: PREPARE TO STOP (or proceed with caution if already in intersection)")
    elif color == "green":
        print("Traffic Light: GREEN")
        print("Action: GO")
    else:
        print("Invalid color")


def classify_person(age, income, education):
    """Complex nested if-else for person classification."""
    
    if age >= 18:
        print(f"Age: {age} - Adult")
        
        if income > 50000:
            print(f"Income: ${income} - High Income")
            
            if education == "graduate":
                print("Education: Graduate Degree")
                print("✓ Classification: High-earning professional")
            else:
                print(f"Education: {education}")
                print("✓ Classification: High-earning non-professional")
        else:
            print(f"Income: ${income} - Low Income")
            
            if education == "graduate":
                print("Education: Graduate Degree")
                print("! Classification: Educated but lower income")
            else:
                print(f"Education: {education}")
                print("! Classification: Lower income and education")
    else:
        print(f"Age: {age} - Minor")
        print("Note: Financial classification not applicable for minors")


def get_discount(purchase_amount, is_member, is_holiday):
    """Calculate discount using nested if-else."""
    
    discount = 0
    
    if purchase_amount >= 100:
        print(f"Purchase amount: ${purchase_amount}")
        print("Base discount: 10%")
        discount = 10
        
        if is_member:
            print("Member: Yes")
            if is_holiday:
                print("Holiday sale: Yes")
                discount = 20
                print(f"Additional holiday discount applied!")
            else:
                discount = 15
                print("Member discount applied!")
        else:
            if is_holiday:
                print("Member: No")
                print("Holiday sale: Yes")
                discount = 15
                print("Holiday discount applied!")
    else:
        print(f"Purchase amount: ${purchase_amount}")
        print("No discount available (minimum $100 required)")
    
    final_amount = purchase_amount * (1 - discount / 100)
    print(f"Final discount: {discount}%")
    print(f"Final amount: ${final_amount:.2f}\n")


# Main Program
print("=" * 50)
print("NESTED IF-ELSE DEMONSTRATIONS")
print("=" * 50)

print("\n1. STUDENT SCHOLARSHIP ELIGIBILITY")
print("-" * 50)
check_student_eligibility(22, 3.8)
print()
check_student_eligibility(26, 3.6)
print()
check_student_eligibility(17, 3.7)

print("\n2. TRAFFIC LIGHT SYSTEM")
print("-" * 50)
traffic_light_action("red")
print()
traffic_light_action("green")

print("\n3. PERSON CLASSIFICATION")
print("-" * 50)
classify_person(30, 75000, "graduate")
print()
classify_person(25, 35000, "bachelor")

print("\n4. DISCOUNT CALCULATOR")
print("-" * 50)
get_discount(150, True, True)
get_discount(120, False, True)
get_discount(200, True, False)

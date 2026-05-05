import math

def solve_quadratic(a, b, c):
    """Solve quadratic equation ax^2 + bx + c = 0 using the quadratic formula."""
    
    # Check if 'a' is zero
    if a == 0:
        print("Error: 'a' cannot be zero. This is not a quadratic equation.")
        return None
    
    # Calculate discriminant
    discriminant = (b ** 2) - (4 * a * c)
    
    # Check the discriminant
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        return root, root
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return f"{real_part} + {imaginary_part}i", f"{real_part} - {imaginary_part}i"


# Get input from user
print("Solve quadratic equation: ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve and display roots
roots = solve_quadratic(a, b, c)
if roots:
    root1, root2 = roots
    print(f"\nRoots of the equation:")
    print(f"Root 1 = {root1}")
    print(f"Root 2 = {root2}")

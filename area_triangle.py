import math

def area_of_triangle_heron(a, b, c):
    """Calculate the area of a triangle using Heron's formula."""
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    
    # Check if triangle is valid
    if s <= a or s <= b or s <= c:
        return None
    
    # Heron's formula: Area = sqrt(s(s-a)(s-b)(s-c))
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


# Get input from user
print("Enter the lengths of the three sides of the triangle:")
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

# Calculate and display area
area = area_of_triangle_heron(a, b, c)
if area is not None:
    print(f"Area of triangle = {area} square units")
else:
    print("Invalid triangle! The sides do not form a valid triangle.")

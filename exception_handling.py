# exception_handling.py

# Example 1: Basic try/except
try:
    number = int(input("Enter an integer: "))
    print(f"You entered {number}.")
except ValueError:
    print("That is not a valid integer.")

# Example 2: Multiple exception types
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"Result is {result}")
finally:
    print("Calculation attempt finished.")

# Example 3: Raising a custom exception
class NegativeNumberError(Exception):
    pass

try:
    value = int(input("Enter a positive number: "))
    if value < 0:
        raise NegativeNumberError("Negative values are not allowed.")
    print(f"You entered {value}.")
except NegativeNumberError as err:
    print(err)
except ValueError:
    print("Please enter a valid integer.")

# Example 4: Using exceptions in a function

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))

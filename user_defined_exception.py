# user_defined_exception.py

class InvalidAgeError(Exception):
    """Custom exception raised when age is outside valid range."""
    def __init__(self, age, message="Age must be between 0 and 120."):
        self.age = age
        self.message = message
        super().__init__(f"Invalid age {age}: {message}")


def get_user_age():
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        raise InvalidAgeError("not-an-integer", "Age must be a whole number.")

    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return age


try:
    user_age = get_user_age()
    print(f"Your age is {user_age}.")
except InvalidAgeError as ex:
    print(f"Error: {ex}")

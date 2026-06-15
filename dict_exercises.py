# Dictionary Exercises in Python

# Exercise 1: Create a dictionary and print it.
student = {
    "name": "Aisha",
    "age": 20,
    "grade": "A"
}
print("Exercise 1: Student dictionary")
print(student)
print()

# Exercise 2: Access values by key.
print("Exercise 2: Access values")
print("Name:", student["name"])
print("Grade:", student.get("grade"))
print()

# Exercise 3: Add and update keys.
student["city"] = "Lahore"
student["grade"] = "A+"
print("Exercise 3: Add and update")
print(student)
print()

# Exercise 4: Loop through keys and values.
print("Exercise 4: Loop through dictionary")
for key, value in student.items():
    print(key, "=", value)
print()

# Exercise 5: Remove a key.
student.pop("age")
print("Exercise 5: Remove age")
print(student)

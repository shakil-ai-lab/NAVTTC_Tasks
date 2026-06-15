# Tuple Exercises in Python

# Exercise 1: Create a tuple of weekdays and print it.
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("Exercise 1: Weekdays tuple")
print(weekdays)
print()

# Exercise 2: Access elements by index.
print("Exercise 2: First and last weekday")
print("First:", weekdays[0])
print("Last:", weekdays[-1])
print()

# Exercise 3: Count and find an element.
print("Exercise 3: Count and index")
print("Number of weekdays:", len(weekdays))
print("Index of Wednesday:", weekdays.index("Wednesday"))
print()

# Exercise 4: Use tuple unpacking.
first, second, third, fourth, fifth = weekdays
print("Exercise 4: Tuple unpacking")
print(first, second, third, fourth, fifth)
print()

# Exercise 5: Convert list to tuple and back.
colors_list = ["red", "green", "blue"]
colors_tuple = tuple(colors_list)
print("Exercise 5: Convert list to tuple")
print(colors_tuple)
print("Back to list:", list(colors_tuple))

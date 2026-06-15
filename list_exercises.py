# List Exercises in Python

# Exercise 1: Create a list of fruits and print each fruit.
fruits = ["apple", "banana", "cherry", "date"]
print("Exercise 1: Fruit list")
for fruit in fruits:
    print(fruit)
print()

# Exercise 2: Add and remove items from a list.
numbers = [10, 20, 30]
numbers.append(40)
numbers.remove(20)
print("Exercise 2: Add 40 and remove 20")
print(numbers)
print()

# Exercise 3: Access list items by index.
colors = ["red", "green", "blue", "yellow"]
print("Exercise 3: First and last colors")
print("First color:", colors[0])
print("Last color:", colors[-1])
print()

# Exercise 4: Use slicing to get part of a list.
numbers = [1, 2, 3, 4, 5, 6]
print("Exercise 4: Slice numbers 2 through 4")
print(numbers[1:4])
print()

# Exercise 5: Check if an item exists in a list.
letters = ["a", "b", "c", "d"]
search = "c"
print("Exercise 5: Is 'c' in letters?")
print(search, "found" if search in letters else "not found")
print()

# Exercise 6: Loop through a list and print the index and value.
print("Exercise 6: Index and value")
for index, value in enumerate(colors):
    print(index, value)
print()

# Exercise 7: Create a list of numbers and compute the sum.
values = [5, 10, 15, 20]
print("Exercise 7: Sum of values")
print(sum(values))
print()

# Exercise 8: Create a list of mixed values and print the length.
mixed = [1, "two", 3.0, True]
print("Exercise 8: Mixed list length")
print(len(mixed))
print()

# Exercise 9: Sort a list of numbers.
numbers = [4, 1, 7, 3, 9]
numbers.sort()
print("Exercise 9: Sorted numbers")
print(numbers)
print()

# Exercise 10: Use a list comprehension to create squares.
squares = [x * x for x in range(1, 6)]
print("Exercise 10: Squares using list comprehension")
print(squares)

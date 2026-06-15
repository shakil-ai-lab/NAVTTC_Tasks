# Set Exercises in Python

# Exercise 1: Create a set and print it.
fruits = {"apple", "banana", "cherry", "apple"}
print("Exercise 1: Fruit set")
print(fruits)
print()

# Exercise 2: Add and remove items.
fruits.add("date")
fruits.discard("banana")
print("Exercise 2: After add and discard")
print(fruits)
print()

# Exercise 3: Check membership.
print("Exercise 3: Membership test")
print("apple" in fruits)
print("mango" in fruits)
print()

# Exercise 4: Use set operations.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Exercise 4: Set operations")
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print()

# Exercise 5: Convert list with duplicates to a set.
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print("Exercise 5: Unique numbers")
print(unique_numbers)

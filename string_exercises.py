# String Exercises in Python

# Exercise 1: Create and print a string.
message = "Hello, Python!"
print("Exercise 1: Message")
print(message)
print()

# Exercise 2: Get string length and access characters.
print("Exercise 2: Length and indexing")
print("Length:", len(message))
print("First char:", message[0])
print("Last char:", message[-1])
print()

# Exercise 3: Slice a string.
print("Exercise 3: Slicing")
print(message[0:5])
print(message[7:])
print()

# Exercise 4: Change case and replace text.
print("Exercise 4: Case and replace")
print(message.upper())
print(message.lower())
print(message.replace("Python", "World"))
print()

# Exercise 5: Split and join.
words = message.split()
print("Exercise 5: Split and join")
print(words)
print("Joined:", "-".join(words))

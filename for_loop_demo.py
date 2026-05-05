def basic_for_loop():
    """Demonstrate basic for loop with range."""
    print("Basic for loop (1 to 5):")
    for i in range(1, 6):
        print(f"Number: {i}")
    print()


def for_loop_with_list():
    """Demonstrate for loop iterating over a list."""
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Fruits in the list:")
    for fruit in fruits:
        print(f"- {fruit}")
    print()


def for_loop_with_string():
    """Demonstrate for loop iterating over a string."""
    text = "Python"
    print(f"Characters in '{text}':")
    for char in text:
        print(f"- {char}")
    print()


def for_loop_with_enumerate():
    """Demonstrate for loop with enumerate for index and value."""
    colors = ["red", "green", "blue", "yellow"]
    print("Colors with their positions:")
    for index, color in enumerate(colors, start=1):
        print(f"{index}. {color}")
    print()


def nested_for_loops():
    """Demonstrate nested for loops (multiplication table)."""
    print("Multiplication Table (1-3):")
    for i in range(1, 4):
        for j in range(1, 4):
            result = i * j
            print(f"{i} × {j} = {result}", end="\t")
        print()  # New line after each row
    print()


def for_loop_with_break():
    """Demonstrate for loop with break statement."""
    print("Finding first even number in list:")
    numbers = [1, 3, 5, 7, 8, 9, 10]
    for num in numbers:
        if num % 2 == 0:
            print(f"Found first even number: {num}")
            break
        print(f"Checking: {num} (odd)")
    print()


def for_loop_with_continue():
    """Demonstrate for loop with continue statement."""
    print("Skipping odd numbers:")
    for num in range(1, 11):
        if num % 2 != 0:
            continue
        print(f"Even number: {num}")
    print()


def calculate_sum_with_for():
    """Demonstrate for loop for calculating sum."""
    numbers = [10, 20, 30, 40, 50]
    total = 0
    print("Calculating sum of numbers:")
    for num in numbers:
        total += num
        print(f"Adding {num}, current total: {total}")
    print(f"Final sum: {total}")
    print()


def pattern_with_for():
    """Demonstrate for loop creating patterns."""
    print("Creating a triangle pattern:")
    for i in range(1, 6):
        print("*" * i)
    print()


def for_loop_with_step():
    """Demonstrate for loop with step parameter."""
    print("Even numbers from 2 to 10 (step=2):")
    for num in range(2, 11, 2):
        print(f"Even: {num}")
    print()


def reverse_countdown():
    """Demonstrate for loop counting backwards."""
    print("Countdown:")
    for i in range(5, 0, -1):
        print(f"{i}...")
    print("Blast off!")
    print()


# Main Program
print("=" * 60)
print("FOR LOOP DEMONSTRATIONS")
print("=" * 60)

basic_for_loop()
for_loop_with_list()
for_loop_with_string()
for_loop_with_enumerate()
nested_for_loops()
for_loop_with_break()
for_loop_with_continue()
calculate_sum_with_for()
pattern_with_for()
for_loop_with_step()
reverse_countdown()

print("=" * 60)
print("FOR LOOP EXAMPLES COMPLETED")
print("=" * 60)
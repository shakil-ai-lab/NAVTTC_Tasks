def break_example():
    """Demonstrate break statement - stops the loop when condition is met."""
    print("Break Example: Stop when we find number 7")
    numbers = [1, 3, 5, 7, 9, 11]

    for num in numbers:
        print(f"Checking: {num}")
        if num == 7:
            print(f"Found {num}! Stopping the loop.")
            break
        print(f"{num} is not 7, continuing...")
    print()


def continue_example():
    """Demonstrate continue statement - skips current iteration."""
    print("Continue Example: Skip odd numbers, print only even numbers")

    for num in range(1, 11):  # Numbers 1 to 10
        if num % 2 != 0:  # If number is odd
            print(f"Skipping odd number: {num}")
            continue
        print(f"Even number: {num}")
    print()


def break_with_while():
    """Break in while loop - user input validation."""
    print("Break Example with While: Enter numbers until you enter 0")

    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            print("You entered 0. Stopping...")
            break
        print(f"You entered: {num}")
    print()


def continue_with_list():
    """Continue with list - skip negative numbers."""
    print("Continue Example: Skip negative numbers in list")

    numbers = [5, -2, 8, -1, 3, -4, 7]

    for num in numbers:
        if num < 0:
            print(f"Skipping negative: {num}")
            continue
        print(f"Processing positive: {num}")
    print()


def break_find_item():
    """Break example - find first even number."""
    print("Break Example: Find first even number")

    numbers = [1, 3, 5, 6, 7, 8, 9]

    for num in numbers:
        if num % 2 == 0:  # Even number
            print(f"Found first even number: {num}")
            break
        print(f"{num} is odd, checking next...")
    print()


def continue_menu_skip():
    """Continue example - skip certain menu options."""
    print("Continue Example: Process menu items (skip 'cancel')")

    menu_items = ["start", "pause", "cancel", "stop", "restart"]

    for item in menu_items:
        if item == "cancel":
            print(f"Skipping menu item: {item}")
            continue
        print(f"Processing menu item: {item}")
    print()


# Main Program
print("=" * 60)
print("BREAK AND CONTINUE STATEMENT EXAMPLES")
print("=" * 60)

break_example()
continue_example()
break_with_while()
continue_with_list()
break_find_item()
continue_menu_skip()

print("=" * 60)
print("BREAK AND CONTINUE EXAMPLES COMPLETED")
print("=" * 60)
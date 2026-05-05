def basic_while_loop():
    """Simple while loop that counts from 1 to 5."""
    print("Basic while loop (counting 1 to 5):")
    count = 1
    while count <= 5:
        print(f"Count: {count}")
        count = count + 1
    print()


def sum_with_while():
    """Calculate sum using while loop."""
    print("Calculating sum of numbers 1 to 5:")
    num = 1
    total = 0
    while num <= 5:
        total = total + num
        print(f"Adding {num}, total now: {total}")
        num = num + 1
    print(f"Final sum: {total}")
    print()


def user_input_loop():
    """Simple loop that asks for user input."""
    print("Enter numbers (enter 0 to stop):")
    total = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        total = total + num
        print(f"Running total: {total}")
    print(f"Final total: {total}")
    print()


def guess_number():
    """Simple number guessing game."""
    print("Guess the number (1-10):")
    secret = 7
    while True:
        guess = int(input("Your guess: "))
        if guess == secret:
            print("Correct! You win!")
            break
        else:
            print("Wrong! Try again.")
    print()


def countdown():
    """Simple countdown using while loop."""
    print("Countdown:")
    num = 5
    while num > 0:
        print(num)
        num = num - 1
    print("Done!")
    print()


def print_even_numbers():
    """Print even numbers using while loop."""
    print("Even numbers from 2 to 10:")
    num = 2
    while num <= 10:
        print(num)
        num = num + 2
    print()


# Main Program
print("=" * 50)
print("SIMPLE WHILE LOOP EXAMPLES")
print("=" * 50)

basic_while_loop()
sum_with_while()
user_input_loop()
guess_number()
countdown()
print_even_numbers()

print("=" * 50)
print("WHILE LOOP EXAMPLES COMPLETED")
print("=" * 50)
import math
# calculate square root of a number by taking input from the user
num = float(input("Enter a number: "))

# calculating the square root
sqrt = num ** 0.5

# displaying the square root
print("The square root of", num, "is", sqrt)

# calculate square root of complex and real numbers 
num2 = complex(input("Enter a complex number (in the form a+bj): "))
sqrt2 = math.sqrt(num2)
print("The square root of", num2, "is", sqrt2)
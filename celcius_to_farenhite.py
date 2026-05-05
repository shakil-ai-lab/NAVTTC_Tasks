def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Get input from user
celsius = float(input("Enter temperature in Celsius: "))

# Convert and display
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")

def kilometers_to_miles(kilometers):
    """Convert distance from kilometers to miles."""
    # 1 kilometer = 0.621371 miles
    miles = kilometers * 0.621371
    return miles


# Get input from user
kilometers = float(input("Enter distance in kilometers: "))

# Convert and display
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} km = {miles:.2f} miles")

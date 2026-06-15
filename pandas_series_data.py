import pandas as pd

# 1. Create synthetic Series data
scores = pd.Series([88, 92, 77, 85], index=['Alice', 'Bob', 'Charlie', 'Diana'])
print("Series data:")
print(scores)
print()

# Access values and index
print("Values:", scores.values)
print("Index:", scores.index)
print("Bob's score:", scores['Bob'])
print()

# Arithmetic operations on Series
bonus = pd.Series([5, 3, 4, 6], index=['Alice', 'Bob', 'Charlie', 'Diana'])
adjusted_scores = scores + bonus
print("Adjusted scores with bonus:")
print(adjusted_scores)
print()

# Filter and sort Series
high_scores = adjusted_scores[adjusted_scores >= 90]
print("High scores (>= 90):")
print(high_scores)
print()

sorted_scores = adjusted_scores.sort_values(ascending=False)
print("Sorted adjusted scores:")
print(sorted_scores)

import pandas as pd

# Synthetic dataset for statistics examples
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George'],
    'MathScore': [82, 90, 78, 90, 85, 78, 88],
    'ReadingScore': [88, 92, 80, 95, 90, 80, 85]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)
print()

# Mean
mean_math = df['MathScore'].mean()
mean_reading = df['ReadingScore'].mean()
print(f"Mean Math score: {mean_math}")
print(f"Mean Reading score: {mean_reading}")
print()

# Median
median_math = df['MathScore'].median()
median_reading = df['ReadingScore'].median()
print(f"Median Math score: {median_math}")
print(f"Median Reading score: {median_reading}")
print()

# Mode
mode_math = df['MathScore'].mode()
mode_reading = df['ReadingScore'].mode()
print("Mode Math score:")
print(mode_math.tolist())
print("Mode Reading score:")
print(mode_reading.tolist())
print()

# Standard deviation
std_math = df['MathScore'].std()
std_reading = df['ReadingScore'].std()
print(f"Standard deviation of Math scores: {std_math:.2f}")
print(f"Standard deviation of Reading scores: {std_reading:.2f}")
print()

# Additional summary statistics
print("Summary statistics for numeric columns:")
print(df[['MathScore', 'ReadingScore']].describe())

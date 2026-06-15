import pandas as pd

# 5. Pandas data cleaning techniques with synthetic dataset
dirty_data = {
    'Name': ['Alice ', 'Bob', None, 'Diana', 'Ethan', 'Alice', 'Frank'],
    'Age': ['25', 'thirty', '22', '28', None, '25', '40'],
    'City': ['New York', 'London', 'Paris', 'New York', 'Paris', 'New York', 'Berlin'],
    'Income': [55000, 62000, 48000, 59000, 61000, 55000, None],
    'SignupDate': ['2024-01-10', '2024-02-05', '2024/03/01', '2024-01-28', '', '2024-01-10', '2024-04-02']
}

dirty_df = pd.DataFrame(dirty_data)
print("Raw dirty data:")
print(dirty_df)
print()

# 1. Trim whitespace and normalize names
dirty_df['Name'] = dirty_df['Name'].astype('string').str.strip()

# 2. Convert Age to numeric; invalid values become NaN
dirty_df['Age'] = pd.to_numeric(dirty_df['Age'], errors='coerce')

# 3. Standardize date format and parse missing values
dirty_df['SignupDate'] = pd.to_datetime(dirty_df['SignupDate'], errors='coerce', infer_datetime_format=True)

# 4. Remove exact duplicate rows
dirty_df = dirty_df.drop_duplicates()

# 5. Fill missing numeric values with median
dirty_df['Age'] = dirty_df['Age'].fillna(dirty_df['Age'].median())
dirty_df['Income'] = dirty_df['Income'].fillna(dirty_df['Income'].median())

print("Cleaned data:")
print(dirty_df)
print()

# 6. Validate cleaned data
print("Data types after cleaning:")
print(dirty_df.dtypes)
print()

# Save cleaned dataset to CSV
csv_path = 'synthetic_dirty_data.csv'
dirty_df.to_csv(csv_path, index=False)
print(f"Saved cleaned dirty data to {csv_path}")

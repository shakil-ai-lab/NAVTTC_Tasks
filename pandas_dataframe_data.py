import pandas as pd

# 2. Create synthetic DataFrame
employees = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Department': ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance'],
    'Salary': [65000, 72000, 88000, 59000, 75000],
    'StartYear': [2018, 2017, 2020, 2019, 2021]
}
df = pd.DataFrame(employees)
print("Synthetic employee DataFrame:")
print(df)
print()
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print()

# Basic DataFrame operations
print("First two rows:")
print(df.head(2))
print()
print("Salaries:")
print(df['Salary'])
print()

# Save DataFrame to CSV
csv_path = 'synthetic_employee_data.csv'
df.to_csv(csv_path, index=False)
print(f"Saved synthetic DataFrame to {csv_path}")

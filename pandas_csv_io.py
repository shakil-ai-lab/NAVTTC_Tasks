import pandas as pd

# 3. Read synthetic CSV data
csv_path = 'synthetic_sales_data.csv'
df = pd.read_csv(csv_path)
print("Sales data loaded from CSV:")
print(df)
print()

print("Data types:")
print(df.dtypes)
print()
print("Summary stats:")
print(df.describe(include='all'))
print()

# Query the CSV data
eu_sales = df[df['Region'] == 'Europe']
print("Europe sales rows:")
print(eu_sales)
print()

# Save a filtered subset if needed
filtered_path = 'synthetic_sales_data_europe.csv'
eu_sales.to_csv(filtered_path, index=False)
print(f"Saved Europe subset to {filtered_path}")

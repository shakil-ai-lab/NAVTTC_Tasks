import pandas as pd
from io import StringIO

# Pandas Basics
print("Pandas version:", pd.__version__)

# 1. Pandas Series data
series_data = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series data:")
print(series_data)
print("Series values:", series_data.values)
print("Series index:", series_data.index)
print("Series element by label:", series_data['b'])
print("Series element by position:", series_data.iloc[2])
print()

# 2. Pandas DataFrame
frame_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(frame_data)
print("DataFrame:")
print(df)
print("DataFrame shape:", df.shape)
print("DataFrame columns:", df.columns)
print("First row:\n", df.iloc[0])
print("Age column:\n", df['Age'])
print()

# 3. Open CSV files
csv_text = "Name,Age,City\nAlice,25,New York\nBob,30,London\nCharlie,35,Paris\n"
csv_buffer = StringIO(csv_text)
csv_df = pd.read_csv(csv_buffer)
print("CSV loaded into DataFrame:")
print(csv_df)

# Save to a CSV file and read it back (uncomment to use file I/O)
# csv_path = 'sample_data.csv'
# df.to_csv(csv_path, index=False)
# df_from_csv = pd.read_csv(csv_path)
# print("DataFrame loaded from file:")
# print(df_from_csv)

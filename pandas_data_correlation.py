import pandas as pd

# 6. Pandas data correlation with synthetic numeric dataset
correlation_data = {
    'StudyHours': [2, 4, 3, 5, 8, 7, 6, 9, 4, 10],
    'Attendance': [60, 70, 68, 75, 90, 85, 80, 92, 72, 95],
    'HomeworkScore': [55, 63, 60, 70, 88, 82, 78, 91, 65, 96],
    'ExamScore': [58, 65, 62, 72, 90, 85, 80, 93, 68, 97]
}

corr_df = pd.DataFrame(correlation_data)
print("Correlation dataset:")
print(corr_df)
print()

# Compute correlation matrix
corr_matrix = corr_df.corr()
print("Correlation matrix:")
print(corr_matrix)
print()

# Pairwise correlations of exam score
print("Correlation with ExamScore:")
print(corr_matrix['ExamScore'].sort_values(ascending=False))
print()

# Identify strongest predictor
strongest_predictor = corr_matrix['ExamScore'].drop('ExamScore').idxmax()
print(f"Strongest predictor of ExamScore: {strongest_predictor}")
print()

# Save dataset to CSV for correlation analysis
csv_path = 'synthetic_correlation_data.csv'
corr_df.to_csv(csv_path, index=False)
print(f"Saved correlation dataset to {csv_path}")

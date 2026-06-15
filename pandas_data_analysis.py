import pandas as pd

# 4. Pandas data analysis with synthetic dataset
marketing_data = {
    'Campaign': ['Email', 'Search', 'Social', 'Referral', 'Display'],
    'Impressions': [12000, 18000, 15000, 5000, 9000],
    'Clicks': [820, 1050, 920, 210, 480],
    'Conversions': [52, 68, 47, 10, 18],
    'Spend': [450, 760, 610, 160, 280]
}

analysis_df = pd.DataFrame(marketing_data)
print("Marketing analysis DataFrame:")
print(analysis_df)
print()

# Add new computed columns
analysis_df['CTR'] = (analysis_df['Clicks'] / analysis_df['Impressions']) * 100
analysis_df['ConversionRate'] = (analysis_df['Conversions'] / analysis_df['Clicks']) * 100
analysis_df['CPA'] = analysis_df['Spend'] / analysis_df['Conversions']

print("Computed metrics:")
print(analysis_df[['Campaign', 'CTR', 'ConversionRate', 'CPA']])
print()

# Summary statistics
print("Summary statistics:")
print(analysis_df.describe())
print()

# Compare campaign performance
best_ctr = analysis_df.loc[analysis_df['CTR'].idxmax()]
print("Best CTR campaign:")
print(best_ctr)
print()

# Save synthetic analysis dataset to CSV
csv_path = 'synthetic_marketing_data.csv'
analysis_df.to_csv(csv_path, index=False)
print(f"Saved marketing analysis dataset to {csv_path}")

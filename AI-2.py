import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe(include='all'))
print("\nFilter rows where Age > 30:")
filtered_df = df[df['Age'] > 30]
print(filtered_df)
print("\nAdd a new column (Salary):")
df['Salary'] = [70000, 80000, 90000, 100000]
print(df)
print("\nSave DataFrame to a CSV file:")
df.to_csv('output.csv', index=False)
print("DataFrame saved to 'output.csv'")

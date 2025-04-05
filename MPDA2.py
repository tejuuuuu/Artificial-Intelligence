import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
downloads_path = os.path.expanduser("~/Downloads/mark.csv")
df = pd.read_csv(downloads_path)
print(df.head())
print(df.info())
if 'Income' in df.columns:
    df['Income'] = df['Income'].fillna(df['Income'].median())
df = df.drop_duplicates()
print(df.describe())
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Income', y='MntTotal', hue='AcceptedCmpOverall')
plt.title('Total Spending vs. Income by Campaign Acceptance')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Kidhome', y='NumWebPurchases')
plt.title('Web Purchases by Kids at Home')
plt.show()
from scipy.stats import ttest_ind
accepted = df[df['Response'] == 1]['MntTotal']
not_accepted = df[df['Response'] == 0]['MntTotal']
t_stat, p_value = ttest_ind(accepted, not_accepted)
print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")
from scipy.stats import f_oneway
valid_groups = [group for i, group in df.groupby('AcceptedCmpOverall')["MntTotal"] if len(group) > 20]
f_stat, p_value = f_oneway(*valid_groups)
print(f"Adjusted ANOVA F-statistic: {f_stat:.2f}, P-value: {p_value:.4f}")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
sns.boxplot(ax=axes[0, 0], data=df, x='AcceptedCmpOverall', y='MntTotal')
axes[0, 0].set_title('Spending by Campaign Acceptance')
sns.scatterplot(ax=axes[0, 1], data=df, x='Income', y='NumWebPurchases', hue='Kidhome')
axes[0, 1].set_title('Web Purchases vs. Income')
sns.barplot(ax=axes[1, 0], data=df, x='Kidhome', y='MntTotal')
axes[1, 0].set_title('Spending by Kids at Home')
sns.histplot(ax=axes[1, 1], data=df, x='Recency', hue='Response', multiple='stack')
axes[1, 1].set_title('Recency by Latest Campaign Response')
plt.tight_layout()
plt.show()


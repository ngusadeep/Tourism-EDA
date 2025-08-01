# Better visualizations for total_cost (numerical variable)
# Add these cells to your notebook for comprehensive total_cost analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (adjust path as needed)
data = pd.read_csv('./datasets/Train.csv')

# 1. Histogram to see distribution
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data=data, x='total_cost', bins=30, kde=True, color='skyblue')
plt.title('Distribution of Total Cost', fontsize=14)
plt.xlabel('Total Cost')
plt.ylabel('Frequency')

# 2. Box plot to see outliers and quartiles
plt.subplot(1, 2, 2)
sns.boxplot(data=data, y='total_cost', color='lightgreen')
plt.title('Box Plot of Total Cost', fontsize=14)
plt.ylabel('Total Cost')
plt.tight_layout()
plt.show()

# 3. Violin plot to see distribution shape
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, y='total_cost', color='lightcoral')
plt.title('Violin Plot of Total Cost Distribution', fontsize=14)
plt.ylabel('Total Cost')
plt.show()

# 4. Cost distribution by different categories
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Cost by age group
sns.boxplot(data=data, x='age_group', y='total_cost', ax=axes[0,0], palette='viridis')
axes[0,0].set_title('Total Cost by Age Group')
axes[0,0].tick_params(axis='x', rotation=45)

# Cost by purpose
sns.boxplot(data=data, x='purpose', y='total_cost', ax=axes[0,1], palette='viridis')
axes[0,1].set_title('Total Cost by Purpose')
axes[0,1].tick_params(axis='x', rotation=45)

# Cost by main activity
sns.boxplot(data=data, x='main_activity', y='total_cost', ax=axes[1,0], palette='viridis')
axes[1,0].set_title('Total Cost by Main Activity')
axes[1,0].tick_params(axis='x', rotation=45)

# Cost by payment mode
sns.boxplot(data=data, x='payment_mode', y='total_cost', ax=axes[1,1], palette='viridis')
axes[1,1].set_title('Total Cost by Payment Mode')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# 5. Statistical summary of total_cost
print("=== Total Cost Statistics ===")
print(f"Mean: ${data['total_cost'].mean():,.2f}")
print(f"Median: ${data['total_cost'].median():,.2f}")
print(f"Standard Deviation: ${data['total_cost'].std():,.2f}")
print(f"Minimum: ${data['total_cost'].min():,.2f}")
print(f"Maximum: ${data['total_cost'].max():,.2f}")
print(f"25th Percentile: ${data['total_cost'].quantile(0.25):,.2f}")
print(f"75th Percentile: ${data['total_cost'].quantile(0.75):,.2f}")

# 6. Cost ranges analysis
cost_ranges = pd.cut(data['total_cost'], bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
cost_distribution = cost_ranges.value_counts().sort_index()

plt.figure(figsize=(10, 6))
cost_distribution.plot(kind='bar', color='teal')
plt.title('Distribution of Total Cost Ranges', fontsize=14)
plt.xlabel('Cost Range')
plt.ylabel('Number of Visitors')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Scatter plot: Cost vs Nights stayed
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(data['night_mainland'], data['total_cost'], alpha=0.6, color='blue')
plt.xlabel('Nights on Mainland')
plt.ylabel('Total Cost')
plt.title('Total Cost vs Nights on Mainland')

plt.subplot(1, 2, 2)
plt.scatter(data['night_zanzibar'], data['total_cost'], alpha=0.6, color='orange')
plt.xlabel('Nights in Zanzibar')
plt.ylabel('Total Cost')
plt.title('Total Cost vs Nights in Zanzibar')

plt.tight_layout()
plt.show()

# 8. Additional insights: Top countries by average cost
country_avg_cost = data.groupby('country')['total_cost'].agg(['mean', 'count']).sort_values('mean', ascending=False)
print("\n=== Top 10 Countries by Average Total Cost ===")
print(country_avg_cost.head(10))

# 9. Cost distribution by travel companions
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='travel_with', y='total_cost', palette='viridis')
plt.title('Total Cost by Travel Companions', fontsize=14)
plt.xlabel('Travel With')
plt.ylabel('Total Cost')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() 
# Fix for the cost analysis code
# Add these lines before the bins calculation:

# Calculate min and max cost values first
min_cost = data['total_cost'].min()
max_cost = data['total_cost'].max()

print(f"Minimum cost: {min_cost}")
print(f"Maximum cost: {max_cost}")

# Then the original code will work:
bins = np.linspace(min_cost, max_cost, 6)  # 5 equal ranges
labels = [f"{int(bins[i])}-{int(bins[i+1])}" for i in range(len(bins)-1)]

data['cost_range'] = pd.cut(data['total_cost'], bins=bins, labels=labels)

plt.figure(figsize=(16, 6))
sns.countplot(x='cost_range', data=data, palette='magma')
plt.title("Visitor Count by Spending Ranges")
plt.xlabel("Spending Range (Min–Max Bins)")
plt.ylabel("Number of Visitors")
plt.show() 
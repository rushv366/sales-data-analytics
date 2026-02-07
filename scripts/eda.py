import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('../data/sales_data_cleaned.csv')

# Top-selling products
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print(top_products.head(10))

# Plot top 10 products
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.head(10).index, y=top_products.head(10).values)
plt.title('Top 10 Products by Revenue')
plt.xticks(rotation=45)
plt.show()

# Sales over time
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()
monthly_sales.plot(kind='line', figsize=(12,6), marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

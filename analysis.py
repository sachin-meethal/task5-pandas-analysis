import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('sales.csv')

# Preview data
print("First 5 rows:")
print(df.head())

# Group and summarize
sales_by_product = df.groupby('product_name')['sales'].sum().sort_values(ascending=False)
print("\nSales by Product:")
print(sales_by_product)

# Plot bar chart
sales_by_product.plot(kind='bar')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

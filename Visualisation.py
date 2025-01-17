import pandas as pd
import matplotlib.pyplot as plt
from data_cleaning import clean_data

# Load the cleaned data using the clean_data function from the data_cleaning module.
df = clean_data()

# 1 - Yearly Sales Analysis

# Extract the year from the 'order_date' column and store it in a new column 'order_year'.
df['order_year'] = df['order_date'].dt.year

# Group the data by 'order_year' and calculate the total sales for each year.
yearly_sales = df.groupby('order_year')['sales'].sum()

# Create a line plot to visualize yearly sales trends.
plt.figure(figsize=(10, 6))
plt.plot(yearly_sales.index, yearly_sales.values, marker='o', linestyle='-', color='b', label='Yearly Sales')
plt.title('Yearly Sales Trends', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 2 - Regional Sales Analysis

# Group the data by 'region' and calculate the total sales for each region.
regional_sales = df.groupby('region')['sales'].sum()

# Create a bar plot to visualize total sales by region.
plt.figure(figsize=(12, 6))
plt.bar(regional_sales.index, regional_sales.values, color='skyblue')
plt.title('Total Sales by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 3 - Customer Segment Sales Analysis

# Group the data by 'segment' and calculate the total sales for each customer segment.
segment_sales = df.groupby('segment')['sales'].sum()

# Create a bar plot to visualize total sales by customer segment.
plt.figure(figsize=(10, 6))
plt.bar(segment_sales.index, segment_sales.values, alpha=0.7)
plt.title('Total Sales by Customer Segment', fontsize=16)
plt.xlabel('Customer Segment', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 4 - Monthly Sales Trends

# Extract the month and year from the 'order_date' column and store it in 'order_month'.
df['order_month'] = df['order_date'].dt.to_period('M')

# Group the data by 'order_month' and calculate the total sales for each month.
monthly_sales = df.groupby('order_month')['sales'].sum()

# Create a line plot to visualize monthly sales trends.
plt.figure(figsize=(14, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', linestyle='-', color='purple', label='Monthly Sales')
plt.title('Monthly Sales Trends', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=90, ha='right', fontsize=10)  # Rotate x-axis labels for readability.
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# 5 - Yearly Profit Trends

# Group the data by 'order_year' and calculate the total profit for each year.
yearly_profit = df.groupby('order_year')['profit'].sum()

# Create a line plot to visualize yearly profit trends.
plt.figure(figsize=(10, 6))
plt.plot(yearly_profit.index.astype(str), yearly_profit.values, marker='o', linestyle='-', color='g', label='Yearly Profit')
plt.title('Yearly Profit Trends', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Profit', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.show()

# 6 - Top Products by Sales

# Group the data by 'product_name', calculate total sales for each product, and pick the top 10 products.
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)

# Create a horizontal bar plot to visualize the top 10 products by sales.
plt.figure(figsize=(12, 6))
top_products.plot(kind='barh', color='orange')
plt.title('Top 10 Products by Sales', fontsize=16)
plt.xlabel('Total Sales', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.tight_layout()  # Adjust layout to ensure everything fits well.
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#export the cleaned DataFrame to a csv file
df.to_csv('cleaned_superstore_data.csv', index=False)
print("\ncleaned Data has been exported to 'cleaned_superstore_data.csv' ")
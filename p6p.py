import pandas as pd

#sample data
sales_data = pd.DataFrame({
    'Date': ['2025-05-01', '2025-05-01', '2025-05-02', '2025-05-03', '2025-05-04', '2025-05-04'],
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product A', 'Product B'],
    'Quantity Sold': [10, 5, 7, 3, 15, 8],
    'Revenue ($)': [200, 100, 140, 90, 300, 200]
})

# Save to CSV
sales_data.to_csv('sales_data.csv', index=False)
import pandas as pd

# Load data
sales_data = pd.read_csv('sales_data.csv')

#Calculate
total_revenue = sales_data['Revenue ($)'].sum()
best_seller = sales_data.groupby('Product')['Quantity Sold'].sum().idxmax()
best_day = sales_data.groupby('Date')['Quantity Sold'].sum().idxmax()

#display results
summary = f"""Sales Analysis Report
-----------------------------
Total Revenue: ${total_revenue}
Best-Selling Product: {best_seller}
Peak Sales Day: {best_day}"""

with open('sales_summary.txt', 'w') as f:
    f.write(summary)

print(summary)

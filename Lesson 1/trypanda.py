import pandas as pd


data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Product': ['laptop', 'Mouse', 'keyboard', 'laptop', 'monitor', 'mouse', 'keyboard', 'monitor'],
    'Category': ['electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Electronics'],
    'Price': [1200, 25, 75, 1200, 300, 25, 75, 300],
    'Quantity': [1, 2, 1, 1, 2, 3, 2, 1],
    'City': ['New York', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],

}
df = pd.DataFrame(data)
print(df.head())
print(df.describe())
ny_orders = df[df['City'] == 'New York']
print(ny_orders)

category_sales = df.groupby('Category')['Quantity'].sum()
print(category_sales)
df['Total'] = df['Price'] * df['Quantity']
print(df[['Product', 'Total']])
print("grand total revenue: $", df['Total'].sum())

import pandas as pd
df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')

def find_orders_within_range(df, minValue, maxValue):
    """

    :param df: Dataframe
    :param minValue: minimum value
    :param maxValue: maximum value
    :return: list of orders of which the total value lies within [minValue, maxValue]
    """
    #total value of each order
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice']*x['Quantity']*(1-x['Discount'])).sum())
    #filter orders within range
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]    #list of orders with unique OrderID
    unique_orders = df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().to_list()
    return unique_orders

# minValue=float(input('Enter the minimum value for the orders: '))
# maxValue=float(input('Enter the maximum value for the orders: '))
# result = find_orders_within_range(df, minValue, maxValue)
# print("Exercise on page 36 - Slide 04. MLBA-Dữ liệu")
# print('List of orders with values ranging from ', minValue, ' to ', maxValue, ':')
# print(result)
# print("*"*25)

def find_orders_within_range_sort(df, minValue, maxValue, sortType=False):
    """

    :param df: Dataframe
    :param minValue: minimum value
    :param maxValue: maximum value
    :param sortType: True - ascending, False - descending (default)
    :return: list of orders (OrderID - Sum) of which the total value (Sum) lies within [minValue, maxValue]
    and Sorted by sortType
    """
    #total value of each order
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice']*x['Quantity']*(1-x['Discount'])).sum())
    #filter orders within range
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]    #list of orders with unique OrderID
    orders_sorted = orders_within_range.to_frame('Sum').sort_values('Sum', ascending=sortType)
    unique_orders_sorted=list(orders_sorted.drop_duplicates().itertuples(index=True, name=None))
    return unique_orders_sorted

minValue=float(input('Enter the minimum value for the orders: '))
maxValue=float(input('Enter the maximum value for the orders: '))
result = find_orders_within_range_sort(df, minValue, maxValue)
print("Exercise on page 36 - Slide 04. MLBA-Dữ liệu")
print('List of orders with values ranging from ', minValue, ' to ', maxValue, ':')
print("Order ID \t Sum")
for orderid,sum in result:
    print(orderid, " \t\t", sum)
print("*"*25)


def find_top_3_selling_products(df):
    """
    Finds the top 3 selling products based on their total sales value.

    :param df: DataFrame with product sales data.
               Must contain 'ProductID', 'UnitPrice', 'Quantity', and 'Discount' columns.
    :return: A list of the top 3 ProductIDs with the highest total sales value.
    """
    # Calculate the total value for each transaction line
    # The formula is: UnitPrice * Quantity * (1 - Discount)
    df['TotalValue'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])

    # Group by ProductID and sum the TotalValue to get the total sales for each product
    product_sales = df.groupby('ProductID')['TotalValue'].sum()

    # Sort the products by their total sales in descending order and select the top 3
    top_3 = product_sales.sort_values(ascending=False).head(3)
    # print(top_3)
    # The ProductIDs are in the index of the resulting Series. Convert the index to a list.
    return top_3.index.to_list()


# --- Example Usage ---
# Call the function to get the top 3 selling products
top_products = find_top_3_selling_products(df.copy())  # Use a copy to avoid modifying the original df

print("Exercise: Find Top 3 Selling Products")
print("-" * 40)
print("The ProductIDs of the top 3 selling products are:")
print(top_products)
print("-" * 40)


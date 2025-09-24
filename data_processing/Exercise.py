import pandas as pd
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

df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')
minValue=float(input('Enter the minimum value for the orders: '))
maxValue=float(input('Enter the maximum value for the orders: '))
result = find_orders_within_range(df, minValue, maxValue)
print('List of orders with values ranging from ', minValue, ' to ', maxValue, ':')
print(result)
import pandas_read_xml as pdx
df=pdx.read_xml("../datasets/SalesTransactions/SalesTransactions.xml", ['UelSample', 'SalesItem'])
print(df.head())
data=df.iloc[0]
print(data)
print(data[0])
print(data[1])
print(data[1]['OrderID'])

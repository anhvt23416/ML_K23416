import pandas as pd
df=pd.read_json('../datasets/SalesTransactions/SalesData.json',
                encoding='utf8', dtype='unicode')
print(df.head())
print(df.info())
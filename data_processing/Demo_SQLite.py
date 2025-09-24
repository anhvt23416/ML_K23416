import sqlite3
import pandas as pd
sqliteConnection = None

try:
    sqliteConnection = sqlite3.connect('../datasets/databases/Chinook_Sqlite.sqlite')
    cursor=sqliteConnection.cursor()
    print("DB init")

    query = "SELECT * FROM InvoiceLine LIMIT 5;"
    cursor.execute(query)
    df=pd.DataFrame(cursor.fetchall())
    # cursor.close()
    print(df.head())

# Exercise Slide 49/50
    print("*"*40)
    n = int(input("Danh sách Customer có >= N invoice, N="))
    query = f"""
        SELECT
            C.CustomerID, COUNT(C.CustomerID)
        FROM
            Customer AS C
        JOIN
            Invoice AS I ON I.CustomerID = C.CustomerID
        GROUP BY
            C.CustomerID
        HAVING
            COUNT(C.CustomerID) >= {n}
        ORDER BY COUNT(C.CustomerID) DESC;
    """

    cursor.execute(query)
    df=pd.DataFrame(cursor.fetchall())
    # Đặt cột 0 (CustomerID) làm index
    df = df.set_index(0)

    # Đặt tên cho index và cột còn lại (cột 1 - TotalSpending)
    df.index.name = 'CustomerID'
    df.columns = ['Number of Invoice']

    # In kết quả
    print(df.head())

    # Get top n customers with highest invoice value
    print("*"*40)
    n = int(input("Danh sách N Customer giá trị invoice cao nhất, N="))
    query = f"""
        SELECT
            C.CustomerID,
            SUM(IL.Quantity * IL.UnitPrice) AS Value
        FROM
            Customer AS C
        JOIN
            Invoice AS I ON I.CustomerID = C.CustomerID
        JOIN
            InvoiceLine AS IL ON IL.InvoiceID = I.InvoiceID
        GROUP BY
            C.CustomerID
        ORDER BY
            Value DESC
        LIMIT {n};
    """

    cursor.execute(query)
    cursor.execute(query)
    df=pd.DataFrame(cursor.fetchall())
    # Đặt cột 0 (CustomerID) làm index
    df = df.set_index(0)

    # Đặt tên cho index và cột còn lại (cột 1 - TotalSpending)
    df.index.name = 'CustomerID'
    df.columns = ['Value']

    # In kết quả
    print(df)
except sqlite3.Error as error:
    print("Error while connecting to sqlite: ", error)
except Exception as error:
    print("Unexpected error:", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
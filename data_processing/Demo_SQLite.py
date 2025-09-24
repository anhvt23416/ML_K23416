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
    n = int(input("Danh sách Customer có tham gia >= N invoice, N="))
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
            COUNT(C.CustomerID) >= {n};
    """

    cursor.execute(query)
    df=pd.DataFrame(cursor.fetchall())
    cursor.close()
    print(df.head())

except sqlite3.Error as error:
    print("Error while connecting to sqlite: ", error)
except Exception as error:
    print("Unexpected error:", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
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
    cursor.close()
    print(df)

except sqlite3.Error as error:
    print("Error while connecting to sqlite: ", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
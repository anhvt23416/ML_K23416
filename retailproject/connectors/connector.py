import traceback
import mysql.connector

class Connector(object):
    def __init__(self, server="localhost", port=3306, database="k23416_retail", username="root", password="Qw3rty^^"):
        self.server=server
        self.port=port
        self.database=database
        self.username=username
        self.password=password

    # Kết nối CSDL
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password)
            return self.conn
        except:
            self.conn = None
            traceback.print_exc()
        return None

    # Ngắt kết nối
    def disConnect(self):
        if self.conn != None:
            self.conn.close()

    # Truy vấn dữ liệu ứng dụng trong máy học
    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns = cursor.column_names
            return df
        except:
            traceback.print_exc()
        return None

    # Trả về tập các bảng trong CSDL
    def getTablesName(self):
        cursor = self.conn.cursor()
        cursor.execute("Show tables;")
        results = cursor.fetchall()
        tablesName = []
        for item in results:
            tablesName.append([tableName for tableName in item][0])
        return tablesName

    def fetchone(self, sql, val):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, val)
            dataset = cursor.fetchone()
            cursor.close()
            return dataset
        except:
            traceback.print_exc()



    def fetchall(self, sql, val):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql,val)
            dataset = cursor.fetchall()
            cursor.close()
            return dataset
        except:
            traceback.print_exc()

    def insert_update_delete_one(self, sql, val):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, val)
            self.conn.commit()
            result=cursor.rowcount #return the affected row
            cursor.close()
            return result
        except Exception as e:
            print(e)
            traceback.print_exc()

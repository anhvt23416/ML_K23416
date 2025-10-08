class Connector(object):
    def __init__(self, server=None, port=None,database=None, username=None, password=None):
        self.server=server
        self.port=port
        self.database=database
        self.username=username
        self.password=password

    def connect(self):
        try:
            self.conn = mysql.connector.connect()
        except Exception as e:
            print(e)
            traceback.print_exc()

    def queryDataset(self):
        return None
    def getTablesName(self):
        return tablesName

    def fetchone(self, sql, val):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, val)
            dataset=cursor.fetchone()
            cursor.close()
            return dataset
        except:
            traceback.print_exc()
        return None
import mysql.connector
import traceback

host="localhost"
port=3306
database="k23416_retail"
user="root"
password="Qw3rty^^"
try:
    conn = mysql.connector.connect(host=host,
                               port=port,
                               database=database,
                               user=user,
                               password=password)
    print("Connected to MySQL")

except Exception as err:
    print(err)
    traceback.print_exc()
def login_customer(email, password):
    try:
        cursor = conn.cursor()
        sql="SELECT * FROM customer " \
                "where Email='"+email+"' and Password='"+ password+"'"
        cursor.execute(sql)
        dataset=cursor.fetchone()
        if dataset!=None:
            id,name,phone,email,password,isDeleted=dataset
            customer= Customer(ID=id,Name=name,Phone=phone,Email=email,Password=password, isDeleted=isDeleted)
            print(customer)
            print()
        else:
            print("login fail")

        cursor.close()
    except Exception as err:
        print(err)
        traceback.print_exc()

    def disConnect():
        if self.conn is not None:
            cursor.close()
            self.conn.close()

    login_customer(email, password)
login_customer("doo@gmail.com", "123")
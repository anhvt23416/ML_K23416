import mysql.connector

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

# cursor = conn.cursor()
# print("Đăng nhập cho customer")

def login_customer(email, password):
    try:
        cursor = conn.cursor()
        sql="SELECT * FROM customer " \
                "where Email='"+email+"' and Password='"+ password+"'"
        print(sql)

        cursor.execute(sql)
        dataset=cursor.fetchone()
        if dataset!=None:
            id,name,phone,email,password,isDeleted=dataset
            print("Id=",id)
            print("name=",name)
            print("phone=",phone)
            print("email=",email)
            print("isDeleted=",isDeleted)
        else:
            print("login fail")

        cursor.close()
    except Exception as err:
        print(err)
# login_customer("doo@gmail.com", "123")

def login_employee(email, password):
    try:
        cursor = conn.cursor()
        sql="SELECT * FROM employee " \
                "where Email=%s and Password=%s"
        val=(email,password)
        cursor.execute(sql,val)
        dataset=cursor.fetchone()
        if dataset!=None:
            print(dataset)
    except:
        print("login fail")
print("Đăng nhập cho employee")
login_employee("obama@gmail.com", "123")
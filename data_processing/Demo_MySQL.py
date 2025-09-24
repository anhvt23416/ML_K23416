from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

# Lấy giá trị của API_KEY từ biến môi trường
# os.getenv() là cách an toàn để đọc, nó sẽ trả về None nếu không tìm thấy

pw=os.getenv("DB_PASS")
print(pw)

# 1. Khởi tạo ứng dụng Flask
app = Flask(__name__)

# 2. Cấu hình các thông số kết nối CSDL TRƯỚC
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = pw
app.config["MYSQL_DB"] = "Parks_and_Recreation"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3306
# Lưu ý: Các key config của Flask-MySQLDB không có tiền tố "DATABASE_"

# 3. Khởi tạo đối tượng MySQL và gắn nó vào app
mysql = MySQL(app)

# 4. Sử dụng khối 'with app.app_context()' để làm việc với CSDL
try:
    with app.app_context():
        # Kết nối sẽ được quản lý tự động trong khối này
        conn = mysql.connection
        cursor = conn.cursor()
        print("Connected to MySQL database")

        # Sửa lại lỗi cú pháp trong tên bảng của bạn
        cursor.execute("""SELECT * FROM `employee_salary` LIMIT 3""")
        data = cursor.fetchall()

        for row in data:
            for val in row:
                print(val, end="\t")
            print()

        cursor.close()
    print("MySQL connection is closed")

except Exception as e:
    print("error", e)
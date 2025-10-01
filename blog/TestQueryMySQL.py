import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Lấy giá trị của API_KEY từ biến môi trường
# os.getenv() là cách an toàn để đọc, nó sẽ trả về None nếu không tìm thấy

server="localhost"
port=3306
database="StudentManagement"
username="root"
password=os.getenv("DB_PASS")

conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)

try:
    cursor = conn.cursor()

    sql = "select * from student"
    cursor.execute(sql)

    dataset = cursor.fetchall()
    align = '{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code', 'Name', "Age"))
    for item in dataset:
        id = item[0]
        code = item[1]
        name = item[2]
        age = item[3]
        avatar = item[4]
        intro = item[5]
        print(align.format(id, code, name, age))

    cursor.close()
except Exception as e:
    print("error", e)
print("-"*40)
print("Students where 22<=Age<=26")
try:
    cursor = conn.cursor()
    sql = "SELECT * FROM student where Age>=22 and Age<=26"
    cursor.execute(sql)

    dataset = cursor.fetchall()
    align = '{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code', 'Name', "Age"))
    for item in dataset:
        id = item[0]
        code = item[1]
        name = item[2]
        age = item[3]
        avatar = item[4]
        intro = item[5]
        print(align.format(id, code, name, age))

    cursor.close()
except Exception as e:
    print("error", e)

print("-" * 40)
print("Students ordered by ascending Age")
try:
    cursor = conn.cursor()
    sql = "SELECT * FROM student " \
          "order by Age asc"
    cursor.execute(sql)

    dataset = cursor.fetchall()
    align = '{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code', 'Name', "Age"))
    for item in dataset:
        id = item[0]
        code = item[1]
        name = item[2]
        age = item[3]
        avatar = item[4]
        intro = item[5]
        print(align.format(id, code, name, age))

    cursor.close()
except Exception as e:
    print("error", e)

print("-" * 40)
print("Students 22<=Age<=26 ordered by descending Age")
try:
    cursor = conn.cursor()
    sql = "SELECT * FROM student " \
          "where Age>=22 and Age<=26 " \
          "order by Age desc "
    cursor.execute(sql)

    dataset = cursor.fetchall()
    align = '{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code', 'Name', "Age"))
    for item in dataset:
        id = item[0]
        code = item[1]
        name = item[2]
        age = item[3]
        avatar = item[4]
        intro = item[5]
        print(align.format(id, code, name, age))

    cursor.close()
except Exception as e:
    print("error", e)


print("-" * 40)
print("Student where id=1")
try:
    cursor = conn.cursor()
    sql = "SELECT * FROM student " \
          "where ID=1 "

    cursor.execute(sql)

    dataset = cursor.fetchone()
    if dataset != None:
        id, code, name, age, avatar, intro = dataset
        print("Id=", id)
        print("code=", code)
        print("name=", name)
        print("age=", age)

    cursor.close()
except Exception as e:
    print("error", e)

print("-" * 40)
print("PAGING!!!!!")
try:
    cursor = conn.cursor()
    sql = "SELECT count(*) FROM student"
    cursor.execute(sql)
    dataset = cursor.fetchone()
    rowcount = dataset[0]

    limit = 3
    step = 3
    for offset in range(0, rowcount, step):
        sql = f"SELECT * FROM student LIMIT {limit} OFFSET {offset}"
        cursor.execute(sql)

        dataset = cursor.fetchall()
        align = '{0:<3} {1:<6} {2:<15} {3:<10}'
        print(align.format('ID', 'Code', 'Name', "Age"))
        for item in dataset:
            id = item[0]
            code = item[1]
            name = item[2]
            age = item[3]
            avatar = item[4]
            intro = item[5]
            print(align.format(id, code, name, age))

    cursor.close()
except Exception as e:
    print("error", e)

# print("-" * 40)
# print("add new student")
# try:
#     cursor = conn.cursor()
#
#     sql = "insert into student (id, code,name,age) values (%s,%s,%s,%s)"
#
#     val = ("6","sv06", "Tận Tuỵ", 20)
#
#     cursor.execute(sql, val)
#
#     conn.commit()
#
#     print(cursor.rowcount, " record inserted")
#
#     cursor.close()
# except Exception as e:
#     print("error", e)

# try:
#     cursor = conn.cursor()
#
#     sql = "insert into student (code,name,age) values (%s,%s,%s)"
#
#     val = [
#         ("sv08", "Trần Quyết Chiến", 19),
#         ("sv09", "Hồ Thắng", 22),
#         ("sv10", "Hoàng Hà", 25),
#     ]
#
#     cursor.executemany(sql, val)
#
#     conn.commit()
#
#     print(cursor.rowcount, " record inserted")
#
#     cursor.close()
# except Exception as e:
#     print("error", e)

# print("-" * 40)
# print("update student")
# try:
#     cursor = conn.cursor()
#     sql = "update student set name='Hoàng Lão Tà' where Code='sv09'"
#     cursor.execute(sql)
# hoặc
#     sql="update student set name=%s where Code=%s"
#     val=('Hoàng Lão Tà','sv09')

#
#     conn.commit()
#
#     print(cursor.rowcount, " record(s) affected")
#     cursor.close()
#     conn.close()
# except Exception as e:
#     print("error", e)
#
# print("-" * 40)
# print("delete 1 student")
# try:
#     cursor = conn.cursor()
#     sql = "DELETE from student where ID=9"
#     cursor.execute(sql)
#
#     conn.commit()
#
#     print(cursor.rowcount, " record(s) affected")
#     cursor.close()
#     conn.close()
# except Exception as e:
#     print("error", e)

# print("-" * 40)
# print("delete with sql injection")
# try:
#
#     cursor = conn.cursor()
#     sql = "DELETE from student where ID=%s"
#     val = (10,)
#
#     cursor.execute(sql, val)
#
#     conn.commit()
#
#     print(cursor.rowcount, " record(s) affected")
#     cursor.close()
#     conn.close()
# except Exception as e:
#     print("error", e)
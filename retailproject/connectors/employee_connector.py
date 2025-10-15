from retailproject.connectors.connector import Connector
from retailproject.models.employee import Employee
class EmployeeConnector(Connector):
    def login(self, email, password):
        sql="select * from employee where email=%s and password=%s;"
        val=(email, password)
        dataset=self.fetchone(sql,val)
        if dataset==None:
            return None
        emp=Employee(dataset)
        print(emp)
        return emp
    def get_all_employees(self):
        sql="select * from employee;"
        dataset= self.fetchall(sql, None)
        employees=[]
        for emp in dataset:
            employees.append(Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5],emp[6]))
        return employees

    def get_detail_infor(self, id):
        sql="select * from employee where ID=%s and password=%s;"
        val=(id, )
        dataset=self.fetchone(sql,val)
        if dataset==None:
            return None
        emp=Employee(dataset[0],
                     dataset[1],
                     dataset[2],
                     dataset[3],
                     dataset[4],
                     dataset[5],
                     dataset[6])
        print(emp)
        return emp
    def insert_one_employee(self, emp):
        sql="insert into employee (\
            `EmployeeCode`,\
            `Name`,\
            `Phone`,\
            `Email`,\
            `Password`,\
            `IsDeleted`) values (%s,%s,%s,%s,%s,%s);"
        val=(emp.EmployeeCode, emp.Name,emp.Phone,emp.Email,emp.Password,emp.isDeleted)
        result=self.insert(sql,val)
        return result

# host="localhost"
# port=3306
# database="k23416_retail"
# user="root"
# password="Qw3rty^^"
# empconn = EmployeeConnector(server=host, port=port, database=database, username=user, password=password)
# empconn.login(email="obama@gmail.com", password="123")

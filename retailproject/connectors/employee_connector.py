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

# host="localhost"
# port=3306
# database="k23416_retail"
# user="root"
# password="Qw3rty^^"
# empconn = EmployeeConnector(server=host, port=port, database=database, username=user, password=password)
# empconn.login(email="obama@gmail.com", password="123")

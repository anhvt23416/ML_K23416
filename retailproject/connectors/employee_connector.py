from retail_project.employee import Employee
class EmployeeConnector(Connector):
    def login(self, email, password):
        sql="select * from employee where email=%s and password=%s;"
        val=(email, password)
        dataset=self.fetchOne(sql,val)
        if dataset==None:
            return None
        emp=Employee(dataset)
        print(emp)
        return emp

host="localhost"
port=3306
database="k23416_retail"
user="root"
password="Qw3rty^^"
empconn = EmployeeConnector(server=host, port=port, database=database, user=user, password=password)
empconn.login(email="obama@gmail.com", password="123")

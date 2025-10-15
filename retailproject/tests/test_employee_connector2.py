from retailproject.connectors.employee_connector import EmployeeConnector
from retailproject.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp=Employee()
emp.EmployeeCode="Emp888"
emp.Name="DrStone"
emp.Phone="113"
emp.Email="stone@m.c"
emp.Password="123"
emp.isDeleted=0
print(emp)
result=ec.insert_one_employee(emp)
if result>0:
    print("insert success")
else:
    print("insert fail")
from retailproject.connectors.employee_connector import EmployeeConnector
from retailproject.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp=Employee()
# emp.ID=7
# emp.EmployeeCode="Emp888"
# emp.Name="DrStone"
# emp.Phone="113"
# emp.Email="stone@m.c"
# emp.Password="123"
# emp.isDeleted=0
# print(emp)
# result=ec.insert_one_employee(emp)
emp.ID=7
emp.EmployeeCode="Emp888"
emp.Name="Dazai"
emp.Phone="113"
emp.Email="dazai@mafia.port"
emp.Password="bsd"
emp.isDeleted=0
print(emp)
result=ec.update_one_employee(emp)
print(result)
if result>0:
    print("update success")
else:
    print("update fail")
#code is updating and inserting at the same time????
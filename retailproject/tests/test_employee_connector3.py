from retailproject.connectors.employee_connector import EmployeeConnector
from retailproject.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp=Employee()
emp.ID=7
result=ec.delete_one_employee(emp)
if result>0:
    print("delete success")
else:
    print("delete fail! no employee with ID"+str(emp.ID))

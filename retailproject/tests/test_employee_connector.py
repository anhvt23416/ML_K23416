from retailproject.connectors.connector import Connector
from retailproject.connectors.employee_connector import EmployeeConnector

ec = EmployeeConnector()
ec.connect()
# ec.login(email,password)
#
print("List of Employee:")
ds = ec.get_all_employees()
print(ds)

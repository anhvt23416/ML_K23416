from retailproject.connectors.employee_connector import EmployeeConnector

ec = EmployeeConnector()
ec.connect()
ec.login(email,password)

from retailproject.connectors.employee_connector import EmployeeConnector

ec = EmployeeConnector()
ec.connect()
# ec.login(email,password)
#
# print("List of Employee:")
# ds = ec.get_all_employees()
# print(ds)
# for emp in ds:
#     print(emp)


id=3
emp=ec.get_detail_infor(id)
if emp==None:
    print(f"Employee id={id} not found")
else:
    print(emp)
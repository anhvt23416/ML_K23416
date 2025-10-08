class Employee:
    def __init__(self,
                 ID=None,
                 EmployeeCode=None,
                 Name=None,
                 Phone=None,
                 Email=None,
                 Password=None,
                 isDeleted=None):
        self.ID = ID
        self.EmployeeCode = EmployeeCode
        self.Name = Name
        self.Phone = Phone
        self.Email = Email
        self.Password = Password
        self.isDeleted = isDeleted

    def __str__(self):
        return f"{self.ID} {self.EmployeeCode} {self.Name} {self.Phone} {self.Email}"
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from retailproject.connectors.employee_connector import EmployeeConnector
from retailproject.models.employee import Employee
from retailproject.ui.EmployeeMainWindow import Ui_MainWindow


class EmployeeMainWindow(Ui_MainWindow):
    def __init__(self, parent=None):
        self.ec=EmployeeConnector()
        self.ec.connect()
        self.is_completed=False

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.displayEmployeesIntoTable()
        self.is_completed=True
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def displayEmployeesIntoTable(self):
        self.employees = self.ec.get_all_employees()
        self.tableWidgetEmloyee.setRowCount(0)#rm existing data
        #load emp into table:
        for emp in self.employees:
            #get the last row (for appending)
            row = self.tableWidgetEmloyee.rowCount()
            #insert a new row as the last one in the table
            self.tableWidgetEmloyee.insertRow(row)
            item_id = QTableWidgetItem(str(emp.ID))
            self.tableWidgetEmloyee.setItem(row, 0, item_id)
            if emp.isDeleted ==1:
                item_id.setBackground(Qt.GlobalColor.red)
            #Code:
            item_code = QTableWidgetItem(str(emp.EmployeeCode))
            self.tableWidgetEmloyee.setItem(row, 1, item_code)
            #Name:
            item_name = QTableWidgetItem(str(emp.Name))
            self.tableWidgetEmloyee.setItem(row, 2, item_name)
            #Phone:
            item_phone = QTableWidgetItem(str(emp.Phone))
            self.tableWidgetEmloyee.setItem(row, 3, item_phone)
            #Email:
            item_email = QTableWidgetItem(str(emp.Email))
            self.tableWidgetEmloyee.setItem(row, 4, item_email)

    def setupSignalAndSlot(self):
        self.pushButtonNew.clicked.connect(self.clear_all())
        self.tableWidgetEmloyee.itemSelectionChanged.connect(self.show_detail)
        self.pushButtonSave.clicke.connect(self.save_employee)
        self.pushButtonUpdate.clicked.connect(self.update_employee)
        self.pushButtonDelete.clicked.connect(self.delete_employee)
    def clear_all(self):
        self.lineEditID.clear()
        self.lineEditCode.clear()
        self.lineEditName.clear()
        self.lineEditPhone.clear()
        self.lineEditEmail.clear()
        self.lineEditPassword.clear()
        self.checkBoxIsDeleted.clear()
        self.lineEditID.setFocus()

    def show_detail(self):
        if self.is_completed==1:
            return
        row_index = self.tableWidgetEmloyee.currentIndex().row()
        print("you clicked at", row_index)
        id = self.tableWidgetEmloyee.item(row_index, 0).text()
        print("Employee ID:", id)
        emp =self.ec.get_detail_infor(id)
        print("Employee Detail:", emp)
        if emp!=None:
            self.lineEditID.setText(str(emp.ID))
            self.lineEditCode.setText(str(emp.EmployeeCode))
            self.lineEditName.setText(str(emp.Name))
            self.lineEditPhone.setText(str(emp.Phone))
            self.lineEditEmail.setText(str(emp.Email))
            self.lineEditPassword.setText(str(emp.Password))
            if emp.isDeleted ==1:
                self.checkBoxIsDeleted.setChecked(True)
            else:
                self.checkBoxIsDeleted.setChecked(False)

    def save_employee(self):
        self.emp=Employee()
        self.emp.EmployeeCode = self.lineEditCode.text()
        self.emp.Name = self.lineEditName.text()
        self.emp.Phone = self.lineEditPhone.text()
        self.emp.Email = self.lineEditEmail.text()
        self.emp.Password = self.lineEditPassword.text()
        self.emp.isDeleted = 0
        print(self.emp)
        result = self.ec.insert_one_employee(self.emp)
        if result > 0:
            self.displayEmployeesIntoTable()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Too bad... Employee can't be saved")
            msg.setWindowTitle("Insert Failed")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.is_completed=True
    def update_employee(self):
        emp = Employee()
        emp.ID = self.lineEditID.text()
        emp.EmployeeCode = self.lineEditCode.text()
        emp.Name = self.lineEditName.text()
        emp.Phone = self.lineEditPhone.text()
        emp.Email = self.lineEditEmail.text()
        emp.Password = self.lineEditPassword.text()
        print(emp)
        result = self.ec.update_one_employee(self.emp)
        if self.checkBoxIsDeleted.isChecked():
            emp.isDeleted = 1
        else:
            emp.isDeleted = 0
        if result > 0:
            self.displayEmployeesIntoTable()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Too bad... Employee can't be updated")
            msg.setWindowTitle("Update Failed")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.is_completed=True

    def delete_employee(self):
        self.is_completed=False
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Do you want to delete this employee?")
        msg.setWindowTitle("Delete Employee")
        msg.setStandardButtons([QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel])
        isConfirmed = msg.exec()
        print(isConfirmed)
        if isConfirmed:
            emp = Employee()
            emp.ID = self.lineEditID.text()
            result=self.ec.delete_one_employee(emp)
            if result > 0:
                self.displayEmployeesIntoTable()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Too bad... Employee can't be deleted")
                msg.setWindowTitle("Delete Employee")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
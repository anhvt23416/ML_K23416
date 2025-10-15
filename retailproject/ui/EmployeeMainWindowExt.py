from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

from retailproject.connectors.employee_connector import EmployeeConnector
from retailproject.ui.EmployeeMainWindow import Ui_MainWindow


class EmployeeMainWindow(Ui_MainWindow):
    def __init__(self, parent=None):
        self.ec=EmployeeConnector()
        self.ec.connect()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
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
        def clear_all(self):
            self.lineEditId.clear()
            self.lineEditCode.clear()
            self.lineEditName.clear()
            self.lineEditPhone.clear()
            self.lineEditEmail.clear()
            self.lineEditPassword.clear()
            self.lineEditDeleted.clear()
            self.lineEditId.setFocus()

        def show_detail(self):
            row_index = self.tableWidgetEmloyee.currentIndex().row()
            print("you clicked at", row_index)
            id = self.tableWidgetEmloyee.item(row_index, 0).text()
            print("Employee ID:", id)
            emp =self.ec.get_detail_infor(id)
            print("Employee Detail:", emp)
            if emp!=None:
                self.lineEditId.setText(str(emp.ID))
                self.lineEditCode.setText(str(emp.EmployeeCode))
                self.lineEditName.setText(str(emp.Name))
                self.lineEditPhone.setText(str(emp.Phone))
                self.lineEditEmail.setText(str(emp.Email))
                self.lineEditPassword.setText(str(emp.Password))
                if emp.isDeleted ==1:
                    self.checkBoxDeleted.setChecked(True)
                else:
                    self.checkBoxDeleted.setChecked(False)


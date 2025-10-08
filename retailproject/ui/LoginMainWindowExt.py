from PyQt6.QtWidgets import QMessageBox

from retailproject.connectors.employee_connector import EmployeeConnector
from retailproject.ui.LoginMainWindow import Ui_MainWindow

class LoginMainWindow(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlots(self):

        self.pushButton.clicked.connect(self.process_login)

    def process_login(self):
        email=self.lineEdit.text()
        pwd = self.lineEdit_2.text()

        ec = EmployeeConnector()
        ec.connect()
        em=ec.login(email, pwd)
        if em==None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login Failed")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Login Successful")
            msg.setWindowTitle("Login Successful")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)


from retailproject.ui.EmployeeMainWindow import Ui_MainWindow


class EmployeeMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
        self.MainWindow.show()

from PyQt6.QtWidgets import QApplication, QMainWindow

from retailproject.ui.LoginMainWindowExt import LoginMainWindow

app=QApplication([])
login_ui=LoginMainWindow()
login_ui.setupUi(QMainWindow())
login_ui.showWindow()
app.exec()
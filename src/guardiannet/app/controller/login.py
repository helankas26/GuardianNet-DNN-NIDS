from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QMessageBox
from src.guardiannet.app.controller import Dashboard
from src.guardiannet.app.model import Users
from src.guardiannet.app.util import PasswordManager, MongoDBManager, WindowManager
from src.guardiannet.app.view import Ui_loginForm


class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_loginForm()
        self.ui.setupUi(self)
        self.__connectSignalsAndSlots()

        self.show()

    def __connectSignalsAndSlots(self):
        self.ui.btnLogin.clicked.connect(self.__login)

    @pyqtSlot()
    def __login(self):
        username = self.ui.txtUsername.text()
        password = self.ui.txtPassword.text()

        if username == '' or password == '':
            QMessageBox.warning(self, 'Error', 'Please fill out all the fields!')
            return

        try:
            MongoDBManager()
            user = Users.objects(username=username).first()
            if PasswordManager.verifyPassword(password, user.password):
                WindowManager.window = Dashboard()
            else:
                QMessageBox.warning(self, 'Warning', 'Incorrect password!')
        except AttributeError as e:
            QMessageBox.warning(self, 'Warning', 'No user found!')
            print(f"Caught an exception: {type(e).__name__}: {e}")
        except Exception as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")

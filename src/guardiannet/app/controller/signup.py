from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QMessageBox

from src.guardiannet.app.config import SystemInitializer
from src.guardiannet.app.controller import Login
from src.guardiannet.app.util import WindowManager
from src.guardiannet.app.view import Ui_signupForm


class Signup(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_signupForm()
        self.ui.setupUi(self)
        self.__connectSignalsAndSlots()

        self.show()

    def __connectSignalsAndSlots(self):
        self.ui.btnSignUp.clicked.connect(self.__signup)

    @pyqtSlot()
    def __signup(self):
        username = self.ui.txtUsername.text()
        password = self.ui.txtPassword.text()
        confirm_password = self.ui.txtConfirmPassword.text()

        if username == '' or password == '' or confirm_password == '':
            QMessageBox.warning(self, 'Error', 'Please fill out all the fields!')
            return

        if password != confirm_password:
            QMessageBox.warning(self, 'Error', 'Password does not match!')
            return

        answer = QMessageBox.question(self, 'Confirmation', 'Do you want to create account?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer == QMessageBox.StandardButton.Yes:
            if SystemInitializer.initializeSystem(username, password):
                WindowManager.window = Login()
            else:
                QMessageBox.warning(self, 'Error', 'Error initializing system!')
                return

        return

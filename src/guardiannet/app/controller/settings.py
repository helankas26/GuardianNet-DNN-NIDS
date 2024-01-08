from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QMessageBox

from src.guardiannet.app.model import Users
from src.guardiannet.app.util import ConfigurationManager, MongoDBManager, SessionManager, PasswordManager, \
    NetworkInterfaceUtil
from src.guardiannet.app.view import Ui_settingsForm


class Settings(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_settingsForm()
        self.ui.setupUi(self)
        self.__setConfiguration()
        self.__connectSignalsAndSlots()

        # self.show()

    def __setConfiguration(self):
        config = ConfigurationManager.loadConfiguration()
        self.ui.cmbBatchSize.addItems(config.get('comboBox').get('cmbBatchSize'))
        self.ui.cmbBatchSize.setCurrentText(str(config.get('setting').get('batchSize')))

        interfaces = NetworkInterfaceUtil.getNetworkInterfaces()
        self.ui.cmbNetworkInterface.addItem("None", None)
        self.ui.cmbNetworkInterface.addItems(interfaces)
        if config.get('setting').get('iface') is None:
            self.ui.cmbNetworkInterface.setCurrentText("None")
        else:
            self.ui.cmbNetworkInterface.setCurrentText(config.get('setting').get('iface'))

    def __connectSignalsAndSlots(self):
        self.ui.btnUpdatePassword.clicked.connect(self.__changePassword)
        self.ui.btnUpdateConfig.clicked.connect(self.__updateConfiguration)

    @pyqtSlot()
    def __changePassword(self):
        password = self.ui.txtPassword.text()
        confirm_password = self.ui.txtConfirmPassword.text()

        if password == '' or confirm_password == '':
            QMessageBox.warning(self, 'Error', 'Please fill out all the fields!')
            return

        if password != confirm_password:
            QMessageBox.warning(self, 'Error', 'Password does not match!')
            return

        answer = QMessageBox.question(self, 'Confirmation', 'Do you want to change password?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer == QMessageBox.StandardButton.Yes:
            try:
                MongoDBManager()
                user = Users.objects(username=SessionManager.user.username).first()

                if user:
                    user.password = PasswordManager.hashPassword(password)
                    user.save()
                else:
                    QMessageBox.warning(self, 'Warning', 'No user found!')
            except AttributeError as e:
                QMessageBox.warning(self, 'Warning', 'No user found!')
                print(f"Caught an exception: {type(e).__name__}: {e}")
            except Exception as e:
                print(f"Caught an exception: {type(e).__name__}: {e}")

    @pyqtSlot()
    def __updateConfiguration(self):
        answer = QMessageBox.question(self, 'Confirmation', 'Do you want to update configuration?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer == QMessageBox.StandardButton.Yes:
            config = ConfigurationManager.loadConfiguration()
            if self.ui.cmbNetworkInterface.currentText() == "None":
                config["setting"]["iface"] = self.ui.cmbNetworkInterface.currentData()
            else:
                config["setting"]["iface"] = self.ui.cmbNetworkInterface.currentText()

            config["setting"]["batchSize"] = int(self.ui.cmbBatchSize.currentText())
            ConfigurationManager.updateConfiguration(config)

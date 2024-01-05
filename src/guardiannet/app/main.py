import sys

from PyQt6.QtWidgets import QApplication

from src.guardiannet.app.controller import Login, Signup
from src.guardiannet.app.util import MongoDBManager, WindowManager, ConfigurationManager


def loadWindow():
    if MongoDBManager.doesDatabaseExist() and ConfigurationManager().doesConfigurationExist():
        return Login()
    else:
        return Signup()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    WindowManager.window = loadWindow()
    sys.exit(app.exec())

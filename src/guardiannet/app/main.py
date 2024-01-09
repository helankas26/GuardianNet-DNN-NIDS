import sys

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from src.guardiannet.app.controller import Login, Signup
from src.guardiannet.app.util import MongoDBManager, WindowManager, ConfigurationManager


def loadWindow():
    if MongoDBManager.doesDatabaseExist() and ConfigurationManager().doesConfigurationExist():
        return Login()
    else:
        return Signup()


def onTrayIconActivated(reason):
    if reason == QSystemTrayIcon.ActivationReason.Trigger:
        WindowManager.window.showNormal()
        WindowManager.window.activateWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(QIcon("assert/logo.png"))
    menu = QMenu()
    exitApp = QAction("EXIT")
    exitApp.triggered.connect(app.quit)
    menu.addAction(exitApp)
    tray.setContextMenu(menu)
    tray.activated.connect(onTrayIconActivated)
    tray.show()

    WindowManager.window = loadWindow()
    sys.exit(app.exec())

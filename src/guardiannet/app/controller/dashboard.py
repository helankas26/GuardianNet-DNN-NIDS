from PyQt6.QtCore import QRect, pyqtSlot, QThread
from PyQt6.QtWidgets import QMainWindow, QStackedLayout

from src.guardiannet.app.controller import Status, Settings, Scan, History
from src.guardiannet.app.util import WindowManager, ScanWorker, HistoryWorker
from src.guardiannet.app.view import Ui_mainWindow


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.__activeNavButton = """
            QPushButton {
                color: #FFF;
                background-color: #E8E8E8;
                border-radius: 10px;
                border: 1px solid #E8E8E8;
            }
    
            QPushButton:pressed {
                background-color: #EBEBEB;
            }
            """

        self.__navButton = """
            QPushButton {
                color: #FFF;
                background-color: #FFF;
                border-radius: 10px;
                border: 1px solid #E8E8E8;
            }
    
            QPushButton:pressed {
                background-color: #EBEBEB;
            }
            """

        self.__setupStackedLayout()
        self.__connectSignalsAndSlots()

        self.scanWorker = ScanWorker()
        self.scanWorkerThread = QThread()
        WindowManager.scanWorker = self.scanWorker
        WindowManager.scanWorkerThread = self.scanWorkerThread

        self.historyWorker = HistoryWorker()
        self.historyWorkerThread = QThread()
        WindowManager.historyWorker = self.historyWorker
        WindowManager.historyWorkerThread = self.historyWorkerThread

        self.show()

    def __setupStackedLayout(self):
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.setGeometry(QRect(0, 0, 990, 650))
        self.stackedLayout.setObjectName("stackedLayout")
        self.stackedLayout.addWidget(Status())
        self.ui.mainFrame.setLayout(self.stackedLayout)
        self.ui.btnStatus.setStyleSheet(self.__activeNavButton)

    def __connectSignalsAndSlots(self):
        self.ui.btnStatus.clicked.connect(lambda: self.__addStackedLayoutWidgets(Status()))
        self.ui.btnHistory.clicked.connect(lambda: self.__addStackedLayoutWidgets(History()))
        self.ui.btnScan.clicked.connect(lambda: self.__addStackedLayoutWidgets(Scan()))
        self.ui.btnSettings.clicked.connect(lambda: self.__addStackedLayoutWidgets(Settings()))

    @pyqtSlot()
    def __addStackedLayoutWidgets(self, widget):
        if isinstance(widget, Scan) and WindowManager.scan is not None:
            self.stackedLayout.removeWidget(self.stackedLayout.currentWidget())
            self.stackedLayout.addWidget(WindowManager.scan)
            self.__changeNavButtonStyle(WindowManager.scan)

            return

        self.stackedLayout.removeWidget(self.stackedLayout.currentWidget())
        self.stackedLayout.addWidget(widget)
        # self.stackedLayout.setCurrentWidget(widget)  # no usage
        self.__changeNavButtonStyle(widget)

    def __changeNavButtonStyle(self, widget):
        self.ui.btnStatus.setStyleSheet(self.__navButton)
        self.ui.btnHistory.setStyleSheet(self.__navButton)
        self.ui.btnScan.setStyleSheet(self.__navButton)
        self.ui.btnSettings.setStyleSheet(self.__navButton)

        match widget:
            case Status():
                self.ui.btnStatus.setStyleSheet(self.__activeNavButton)

            case History():
                self.ui.btnHistory.setStyleSheet(self.__activeNavButton)

            case Scan():
                self.ui.btnScan.setStyleSheet(self.__activeNavButton)

            case Settings():
                self.ui.btnSettings.setStyleSheet(self.__activeNavButton)

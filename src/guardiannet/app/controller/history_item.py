from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget

from src.guardiannet.app.view import Ui_historyItem


class HistoryItem(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_historyItem()
        self.ui.setupUi(self)
        self.__connectSignalsAndSlots()

        # self.show()

    def __connectSignalsAndSlots(self):
        self.ui.btnDownload.clicked.connect(self.__downloadCSV)
        self.ui.btnView.clicked.connect(self.__viewDetails)
        self.ui.btnDelete.clicked.connect(self.__deleteRecord)

    @pyqtSlot()
    def __downloadCSV(self):
        pass

    @pyqtSlot()
    def __viewDetails(self):
        pass

    @pyqtSlot()
    def __deleteRecord(self):
        pass

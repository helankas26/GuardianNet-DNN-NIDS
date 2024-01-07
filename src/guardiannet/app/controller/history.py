from PyQt6.QtCore import pyqtSignal, pyqtSlot, QSize
from PyQt6.QtWidgets import QWidget, QListWidgetItem

from src.guardiannet.app.controller import HistoryItem
from src.guardiannet.app.util import WindowManager
from src.guardiannet.app.view import Ui_historyForm


class History(QWidget):
    work_requested = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_historyForm()
        self.ui.setupUi(self)

        self.historyWorker = WindowManager.historyWorker
        self.workerThread = WindowManager.historyWorkerThread

        self.__connectSignalsAndSlots()

        self.historyWorker.moveToThread(self.workerThread)
        self.workerThread.start()

        self.__emitSigal()

        # self.show()

    def __del__(self):
        self.historyWorker.stopSignal = True

    def __connectSignalsAndSlots(self):
        self.historyWorker.progress.connect(self.__loadHistory)
        self.work_requested.connect(self.historyWorker.loadHistory)

    def __emitSigal(self):
        self.historyWorker.stopSignal = False
        self.work_requested.emit()

    @pyqtSlot()
    def __loadHistory(self):
        newItem = QListWidgetItem(self.ui.recordsListWidget)
        newItem.setSizeHint(QSize(950, 46))
        historyItem = HistoryItem()
        self.ui.recordsListWidget.setItemWidget(newItem, historyItem)

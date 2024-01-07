from PyQt6.QtCore import pyqtSlot, pyqtSignal, QObject


class HistoryWorker(QObject):
    progress = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.stopSignal = False

    @pyqtSlot()
    def loadHistory(self):
        for x in range(200):
            if self.stopSignal:
                break

            self.progress.emit()

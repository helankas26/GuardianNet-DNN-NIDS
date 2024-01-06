import time

from PyQt6.QtCore import pyqtSlot, pyqtSignal, QObject


class ScanWorker(QObject):
    progress = pyqtSignal(int)
    completed = pyqtSignal(int)

    @pyqtSlot(str, str)
    def scan(self, filename, dirname):
        for i in range(0, 101, 10):
            time.sleep(0.5)
            self.progress.emit(i)

        self.completed.emit(i)
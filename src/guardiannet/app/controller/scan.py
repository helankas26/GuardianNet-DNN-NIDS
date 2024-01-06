from PyQt6.QtCore import pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox, QStyleFactory

from src.guardiannet.app.util import WindowManager
from src.guardiannet.app.view import Ui_scanForm


class Scan(QWidget):
    work_requested = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

        self.ui = Ui_scanForm()
        self.ui.setupUi(self)
        self.ui.scanProgressBar.setVisible(False)
        self.ui.scanProgressBar.setStyle(QStyleFactory.create("Fusion"))
        self.filename = None
        self.dirname = None

        self.scanWorker = WindowManager.scanWorker
        self.workerThread = WindowManager.workerThread

        self.__connectSignalsAndSlots()

        self.scanWorker.moveToThread(self.workerThread)
        self.workerThread.start()

        # self.show()

    def __connectSignalsAndSlots(self):
        self.ui.btnOpenFile.clicked.connect(self.__openCaptureFile)
        self.ui.btnBrowse.clicked.connect(self.__selectFileSaveLocation)
        self.ui.btnRunScan.clicked.connect(self.__runScan)

        self.scanWorker.progress.connect(self.__updateProgress)
        self.scanWorker.completed.connect(self.__complete)
        self.work_requested.connect(self.scanWorker.scan)

    @pyqtSlot()
    def __openCaptureFile(self):
        self.filename, _ = QFileDialog.getOpenFileName(
            self,
            caption="Open Capture File",
            directory="",
            filter="Capture Files (*.pcap *.pcapng *.cap)"
        )

        try:
            if self.filename:
                self.ui.txtPcapFilePath.setText(str(self.filename))
        except Exception as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")

    @pyqtSlot()
    def __selectFileSaveLocation(self):
        self.dirname = QFileDialog.getExistingDirectory(
            self,
            "Select a Directory"
        )

        try:
            if self.dirname:
                self.ui.txtOutputFilePath.setText(self.dirname)
        except Exception as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")

    @pyqtSlot()
    def __runScan(self):
        try:
            if self.filename is None:
                QMessageBox.warning(self, 'Warning', 'Please select a capture file!')
                return

            if self.dirname is None:
                QMessageBox.warning(self, 'Warning', 'Please select a folder!')
                return
        except Exception as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")

        answer = QMessageBox.question(self, 'Confirmation', 'Do you want to scan?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer == QMessageBox.StandardButton.Yes:
            try:
                self.ui.btnRunScan.setDisabled(True)
                self.ui.btnOpenFile.setDisabled(True)
                self.ui.btnBrowse.setDisabled(True)
                self.ui.scanProgressBar.setVisible(True)

                WindowManager.scan = self

                self.work_requested.emit(self.filename, self.dirname)

            except Exception as e:
                print(f"Caught an exception: {type(e).__name__}: {e}")

    @pyqtSlot(int)
    def __updateProgress(self, v):
        self.ui.scanProgressBar.setValue(v)

    @pyqtSlot(int)
    def __complete(self, v):
        self.ui.scanProgressBar.setValue(v)

        self.ui.btnRunScan.setDisabled(False)
        self.ui.btnOpenFile.setDisabled(False)
        self.ui.btnBrowse.setDisabled(False)
        # self.ui.scanProgressBar.setVisible(False)

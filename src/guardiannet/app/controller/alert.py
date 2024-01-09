from PyQt6.QtWidgets import QWidget

from src.guardiannet.app.view import Ui_alertForm


class Alert(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_alertForm()
        self.ui.setupUi(self)
        self.__connectSignalsAndSlots()

        self.show()

    def __connectSignalsAndSlots(self):
        self.ui.btnClose.clicked.connect(self.__close)

    def __close(self):
        self.close()

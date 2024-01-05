from PyQt6.QtWidgets import QWidget

from src.guardiannet.app.view import Ui_statusForm


class Status(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_statusForm()
        self.ui.setupUi(self)

        # self.show()

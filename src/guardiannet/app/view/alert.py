# Form implementation generated from reading ui file 'alert.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_alertForm(object):
    def setupUi(self, alertForm):
        alertForm.setObjectName("alertForm")
        alertForm.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        alertForm.setWindowIcon(icon)
        alertForm.setStyleSheet("#alertForm {\n"
"border-radius: 16px;\n"
"background: #555;\n"
"border: 1px solid #dddddd;\n"
"}")
        self.alertFrame = QtWidgets.QFrame(parent=alertForm)
        self.alertFrame.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.alertFrame.setStyleSheet("#alertFrame {\n"
"border-radius: 16px;\n"
"background: #555;\n"
"border: 1px solid #dddddd;\n"
"}")
        self.alertFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.alertFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.alertFrame.setObjectName("alertFrame")
        self.alertImg = QtWidgets.QLabel(parent=self.alertFrame)
        self.alertImg.setGeometry(QtCore.QRect(200, 50, 100, 100))
        self.alertImg.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border-color :transparent;\n"
"}")
        self.alertImg.setText("")
        self.alertImg.setPixmap(QtGui.QPixmap("assert/warning.png"))
        self.alertImg.setScaledContents(True)
        self.alertImg.setObjectName("alertImg")
        self.label = QtWidgets.QLabel(parent=self.alertFrame)
        self.label.setGeometry(QtCore.QRect(90, 180, 320, 40))
        self.label.setStyleSheet("QLabel {\n"
"color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"background-color: transparent;\n"
"border-color :transparent;\n"
"}")
        self.label.setObjectName("label")
        self.btnClose = QtWidgets.QPushButton(parent=self.alertFrame)
        self.btnClose.setEnabled(True)
        self.btnClose.setGeometry(QtCore.QRect(175, 310, 150, 35))
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    background-color: #BCBCBC;\n"
"    font-family: Inter;\n"
"    font-size: 22px;\n"
"    font-style: normal;\n"
"    font-weight: 500;\n"
"    line-height: normal;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(208, 208, 208);\n"
"}")
        self.btnClose.setObjectName("btnClose")
        self.lblAttcak = QtWidgets.QLabel(parent=self.alertFrame)
        self.lblAttcak.setGeometry(QtCore.QRect(125, 225, 250, 40))
        self.lblAttcak.setStyleSheet("QLabel {\n"
"color: #FE0000;\n"
"font-family: Inter;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 550;\n"
"background-color: transparent;\n"
"border-color :transparent;\n"
"}")
        self.lblAttcak.setObjectName("lblAttcak")

        self.retranslateUi(alertForm)
        QtCore.QMetaObject.connectSlotsByName(alertForm)

    def retranslateUi(self, alertForm):
        _translate = QtCore.QCoreApplication.translate
        alertForm.setWindowTitle(_translate("alertForm", "Alert"))
        self.label.setText(_translate("alertForm", "Attack has been detected"))
        self.btnClose.setText(_translate("alertForm", "Close"))
        self.lblAttcak.setText(_translate("alertForm", "DoS Slowhttptest"))

# Form implementation generated from reading ui file 'status_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_statusForm(object):
    def setupUi(self, statusForm):
        statusForm.setObjectName("statusForm")
        statusForm.resize(990, 650)
        statusForm.setMinimumSize(QtCore.QSize(990, 650))
        statusForm.setMaximumSize(QtCore.QSize(990, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        statusForm.setWindowIcon(icon)
        statusForm.setStyleSheet("QWidget {\n"
"border-radius: 16px;\n"
"background: #FFF;\n"
"border: 1px solid #dddddd;\n"
"}")
        self.statusFrame = QtWidgets.QFrame(parent=statusForm)
        self.statusFrame.setGeometry(QtCore.QRect(10, 10, 970, 233))
        self.statusFrame.setStyleSheet("QFrame {\n"
"border-radius: 10px;\n"
"background: #EFF7EB;\n"
"border: 1px solid #dddddd;\n"
"}")
        self.statusFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.statusFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.statusFrame.setObjectName("statusFrame")
        self.statusImg = QtWidgets.QLabel(parent=self.statusFrame)
        self.statusImg.setGeometry(QtCore.QRect(435, 20, 100, 100))
        self.statusImg.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border-color :transparent;\n"
"}")
        self.statusImg.setText("")
        self.statusImg.setPixmap(QtGui.QPixmap("assert/protected.png"))
        self.statusImg.setScaledContents(True)
        self.statusImg.setObjectName("statusImg")
        self.label = QtWidgets.QLabel(parent=self.statusFrame)
        self.label.setGeometry(QtCore.QRect(260, 140, 241, 41))
        self.label.setStyleSheet("QLabel {\n"
"color: #000;\n"
"font-family: Calibri;\n"
"font-size: 36px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: transparent;\n"
"border-color :transparent;\n"
"}")
        self.label.setObjectName("label")
        self.lblStatus = QtWidgets.QLabel(parent=self.statusFrame)
        self.lblStatus.setGeometry(QtCore.QRect(495, 140, 231, 41))
        self.lblStatus.setStyleSheet("QLabel {\n"
"color: #3BA44C;\n"
"font-family: Calibri;\n"
"font-size: 36px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: transparent;\n"
"border-color :transparent;\n"
"}")
        self.lblStatus.setObjectName("lblStatus")
        self.barChartFrame = QtWidgets.QFrame(parent=statusForm)
        self.barChartFrame.setGeometry(QtCore.QRect(10, 253, 480, 387))
        self.barChartFrame.setStyleSheet("QFrame {\n"
"border-radius: 10px;\n"
"background: #D9D9D9;\n"
"border: 1px solid #dddddd;\n"
"}")
        self.barChartFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.barChartFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.barChartFrame.setObjectName("barChartFrame")
        self.pieChartFrame = QtWidgets.QFrame(parent=statusForm)
        self.pieChartFrame.setGeometry(QtCore.QRect(500, 253, 480, 387))
        self.pieChartFrame.setStyleSheet("QFrame {\n"
"border-radius: 10px;\n"
"background: #D9D9D9;\n"
"border: 1px solid #dddddd;\n"
"}")
        self.pieChartFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pieChartFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pieChartFrame.setObjectName("pieChartFrame")

        self.retranslateUi(statusForm)
        QtCore.QMetaObject.connectSlotsByName(statusForm)

    def retranslateUi(self, statusForm):
        _translate = QtCore.QCoreApplication.translate
        statusForm.setWindowTitle(_translate("statusForm", "Status"))
        self.label.setText(_translate("statusForm", "This network is"))
        self.lblStatus.setText(_translate("statusForm", "protected"))
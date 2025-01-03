# Form implementation generated from reading ui file 'signup_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_signupForm(object):
    def setupUi(self, signupForm):
        signupForm.setObjectName("signupForm")
        signupForm.setEnabled(True)
        signupForm.resize(870, 510)
        signupForm.setMinimumSize(QtCore.QSize(870, 510))
        signupForm.setMaximumSize(QtCore.QSize(870, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        signupForm.setWindowIcon(icon)
        signupForm.setStyleSheet("background: #EAEAEA;")
        self.loginImage = QtWidgets.QLabel(parent=signupForm)
        self.loginImage.setGeometry(QtCore.QRect(0, 0, 435, 510))
        self.loginImage.setText("")
        self.loginImage.setPixmap(QtGui.QPixmap("assert/signup.png"))
        self.loginImage.setScaledContents(True)
        self.loginImage.setObjectName("loginImage")
        self.frame = QtWidgets.QFrame(parent=signupForm)
        self.frame.setGeometry(QtCore.QRect(480, 30, 341, 431))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background: #FFF;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.logo = QtWidgets.QLabel(parent=self.frame)
        self.logo.setGeometry(QtCore.QRect(110, 30, 116, 139))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("assert/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.name = QtWidgets.QLabel(parent=self.frame)
        self.name.setGeometry(QtCore.QRect(110, 170, 121, 41))
        self.name.setStyleSheet("color: #FF0F0F;\n"
"font-family: Agency FB;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.name.setObjectName("name")
        self.txtUsername = QtWidgets.QLineEdit(parent=self.frame)
        self.txtUsername.setGeometry(QtCore.QRect(70, 220, 200, 27))
        self.txtUsername.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.txtUsername.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 1px solid #B7B7B7;\n"
"    background: #FFF;\n"
"    color: #000;\n"
"    font-family: Inter;\n"
"    font-size: 14px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 1px solid #4383CD;\n"
"}")
        self.txtUsername.setFrame(True)
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(parent=self.frame)
        self.txtPassword.setGeometry(QtCore.QRect(70, 260, 200, 27))
        self.txtPassword.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 1px solid #B7B7B7;\n"
"    background: #FFF;\n"
"    color: #000;\n"
"    font-family: Inter;\n"
"    font-size: 14px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 1px solid #4383CD;\n"
"}")
        self.txtPassword.setFrame(True)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.btnSignUp = QtWidgets.QPushButton(parent=self.frame)
        self.btnSignUp.setEnabled(True)
        self.btnSignUp.setGeometry(QtCore.QRect(97, 350, 150, 35))
        self.btnSignUp.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnSignUp.setStyleSheet("QPushButton {\n"
"    color: #FFF;\n"
"    background-color: rgb(72, 166, 63);\n"
"    font-family: Inter;\n"
"    font-size: 16px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(80, 180, 68);\n"
"}")
        self.btnSignUp.setObjectName("btnSignUp")
        self.txtConfirmPassword = QtWidgets.QLineEdit(parent=self.frame)
        self.txtConfirmPassword.setGeometry(QtCore.QRect(70, 300, 200, 27))
        self.txtConfirmPassword.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 1px solid #B7B7B7;\n"
"    background: #FFF;\n"
"    color: #000;\n"
"    font-family: Inter;\n"
"    font-size: 14px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 1px solid #4383CD;\n"
"}")
        self.txtConfirmPassword.setFrame(True)
        self.txtConfirmPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")

        self.retranslateUi(signupForm)
        QtCore.QMetaObject.connectSlotsByName(signupForm)
        signupForm.setTabOrder(self.txtUsername, self.txtPassword)
        signupForm.setTabOrder(self.txtPassword, self.txtConfirmPassword)
        signupForm.setTabOrder(self.txtConfirmPassword, self.btnSignUp)

    def retranslateUi(self, signupForm):
        _translate = QtCore.QCoreApplication.translate
        signupForm.setWindowTitle(_translate("signupForm", "Signup"))
        self.name.setText(_translate("signupForm", "GuardiaNet"))
        self.txtUsername.setPlaceholderText(_translate("signupForm", "Username"))
        self.txtPassword.setPlaceholderText(_translate("signupForm", "Password"))
        self.btnSignUp.setText(_translate("signupForm", "SignUp"))
        self.txtConfirmPassword.setPlaceholderText(_translate("signupForm", "Confirm Password"))

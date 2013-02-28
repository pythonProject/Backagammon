# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Wed Feb 27 16:32:24 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName(_fromUtf8("LoginForm"))
        LoginForm.resize(500, 357)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        LoginForm.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("favicon.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginForm.setWindowIcon(icon)
        LoginForm.setWindowOpacity(1.0)
        self.lineEdit = QtGui.QLineEdit(LoginForm)
        self.lineEdit.setGeometry(QtCore.QRect(210, 50, 137, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(LoginForm)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 90, 137, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.LabelLogin = QtGui.QLabel(LoginForm)
        self.LabelLogin.setGeometry(QtCore.QRect(31, 51, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelLogin.setFont(font)
        self.LabelLogin.setObjectName(_fromUtf8("LabelLogin"))
        self.LabelPass = QtGui.QLabel(LoginForm)
        self.LabelPass.setGeometry(QtCore.QRect(30, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelPass.setFont(font)
        self.LabelPass.setObjectName(_fromUtf8("LabelPass"))
        self.pushButton = QtGui.QPushButton(LoginForm)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.commandLinkButton = QtGui.QCommandLinkButton(LoginForm)
        self.commandLinkButton.setGeometry(QtCore.QRect(160, 120, 223, 48))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.ErrorLabel = QtGui.QLabel(LoginForm)
        self.ErrorLabel.setGeometry(QtCore.QRect(60, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setObjectName(_fromUtf8("ErrorLabel"))

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(_translate("LoginForm", "Вход/Регистрация", None))
        self.LabelLogin.setText(_translate("LoginForm", "Введите Ваш логин", None))
        self.LabelPass.setText(_translate("LoginForm", "Введите Ваш пароль", None))
        self.pushButton.setText(_translate("LoginForm", "Войти", None))
        self.commandLinkButton.setText(_translate("LoginForm", "Зарегистрироваться", None))
        self.ErrorLabel.setText(_translate("LoginForm", "<html><head/><body><p><span style=\" color:#ff0000;\"></span></p></body></html>", None))

    def LoginError(self, text):
        self.ErrorLabel.setText(_translate("LoginForm", "<html><head/><body><p><span style=\" color:#ff0000;\">" + text + "</span></p></body></html>", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created: Thu Feb 14 14:44:06 2013
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

class Ui_RegistrationForm(object):
    def setupUi(self, RegistrationForm):
        RegistrationForm.setObjectName(_fromUtf8("RegistrationForm"))
        RegistrationForm.setWindowModality(QtCore.Qt.NonModal)
        RegistrationForm.resize(465, 165)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("favicon.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RegistrationForm.setWindowIcon(icon)
        self.LoginRegister = QtGui.QLineEdit(RegistrationForm)
        self.LoginRegister.setGeometry(QtCore.QRect(142, 40, 201, 22))
        self.LoginRegister.setObjectName(_fromUtf8("LoginRegister"))
        self.PassRegister = QtGui.QLineEdit(RegistrationForm)
        self.PassRegister.setGeometry(QtCore.QRect(142, 80, 201, 22))
        self.PassRegister.setObjectName(_fromUtf8("PassRegister"))
        self.PassRegister.setEchoMode(QtGui.QLineEdit.Password)
        self.label = QtGui.QLabel(RegistrationForm)
        self.label.setGeometry(QtCore.QRect(80, 40, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(RegistrationForm)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.RegisterBtn = QtGui.QPushButton(RegistrationForm)
        self.RegisterBtn.setGeometry(QtCore.QRect(140, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RegisterBtn.setFont(font)
        self.RegisterBtn.setObjectName(_fromUtf8("RegisterBtn"))
        self.RegisterError = QtGui.QLabel(RegistrationForm)
        self.RegisterError.setGeometry(QtCore.QRect(60, 10, 352, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.RegisterError.setFont(font)
        self.RegisterError.setObjectName(_fromUtf8("RegisterError"))

        self.retranslateUi(RegistrationForm)
        QtCore.QMetaObject.connectSlotsByName(RegistrationForm)

    def retranslateUi(self, RegistrationForm):
        RegistrationForm.setWindowTitle(_translate("RegistrationForm", "Форма регистриции", None))
        self.label.setText(_translate("RegistrationForm", "Логин", None))
        self.label_2.setText(_translate("RegistrationForm", "Пароль", None))
        self.RegisterBtn.setText(_translate("RegistrationForm", "Зарегистрироваться", None))

    def showError(self, message):
        self.RegisterError.setText(_translate("RegistrationForm", "<html><head/><body><p><span style=\" color:#ff0000;\">" + message + "</span></p></body></html>", None))


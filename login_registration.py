#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys, sqlite3, os
from ui_login_reqister import Ui_LoginForm
from ui_register import Ui_RegistrationForm
import socket

def pathDb():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "backgamon.sql").replace("\\", "/")

def connectDb():
   return sqlite3.connect(pathDb())

class LoginWindow(QtGui.QWidget):

    def __init__(self, sock, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.sock = sock
        self.connect(self.ui.commandLinkButton, QtCore.SIGNAL("clicked()"), self.register_clicked)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.login_clicked)

    def login_clicked(self):
        login = unicode(self.ui.lineEdit.text()).strip()
        passwd = unicode(self.ui.lineEdit_2.text()).strip()
        self.sock.sendall("login: user={0} passwd={1}".format(login, passwd))
        resp = unicode(self.sock.recv(1024))
        if resp is not "OK":
            self.ui.LoginError(u"Вы ввели не правильные детали!!!")
        else:
            return

    def register_clicked(self):
        global registerWindow
        self.sock.sendall("registration")
        registerWindow = RegisterWindow(self.sock)
        registerWindow.show()

    def closeEvent(self, event):
        self.sock.sendall("Exit")
        event.accept()

class RegisterWindow(QtGui.QWidget):
    def __init__(self, sock, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.sock = sock
        self.registrationForm = Ui_RegistrationForm()
        self.registrationForm.setupUi(self)
        self.connect(self.registrationForm.RegisterBtn, QtCore.SIGNAL("clicked()"),
                     lambda : self.registration_start(True))

    def registration_start(self, flag):
        login = unicode(self.registrationForm.LoginRegister.text()).strip()
        password = unicode(self.registrationForm.PassRegister.text()).strip()
        if login == "" or password == "":
            self.registrationForm.showError("Вы не ввели имья пользователя или пароль!!!")
            return
        try:
            f = open(pathDb())
            f.close()
        except IOError:
            with connectDb() as con:
                curr = con.cursor()
                curr.execute(
                    """
                    create table t_user(
                        id integer not null primary key autoincrement,
                        user text null,
                        passwd text null,
                        last_login integer null
                        );
                    """
                    )
                con.commit()
                # con.close()
        err = registerOnServer(login, password, self.sock)
        if err:
            self.registrationForm.showError(err)
            return
        else:
            if not self.register(login, password):
                self.close()

    def register(self, login, password):
        id_list = []
        with connectDb() as conn:
            curr = conn.cursor()
            curr.execute(
            """
            select id from t_user where user = ?;
            """, (unicode(login), )
            )
            for i in curr:
                id_list.append(i)
            print id_list
            if len(id_list) == 0:
                curr.execute(
                    """
                    insert into t_user(user, passwd)
                    values(?, ?);
                    """,(unicode(login), unicode(password), )
                    )
                conn.commit()
            else:
                self.registrationForm.showError("Данный пользователь уже сущесвствует")
                return True

    def closeEvent(self, event):
        self.sock.sendall("finishRegistration")
        event.accept()

def registerOnServer(user, passwd, sock):
    sock.send("user=" + user + " password=" + passwd)
    mess = sock.recv(1024)
    if "ERROR" in mess:
        return mess.split(": ")[1]
    else:
        return False


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

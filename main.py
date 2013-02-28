#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket, sys
from PyQt4 import QtGui
from login_registration import LoginWindow
from conf import HOST, PORT

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall("Login")
    print sock.recv(1024)
    window = LoginWindow(sock=sock)
    window.show()

    sys.exit(app.exec_())
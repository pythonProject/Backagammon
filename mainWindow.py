#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowIcon(QtGui.QIcon("favicon.jpeg"))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Changing of the icon")
    window.resize(300, 50)
    window.show()
    sys.exit(app.exec_())

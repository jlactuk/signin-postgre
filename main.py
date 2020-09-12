# This Python file uses the following encoding: utf-8

#from PyQt5.QtWidgets import QMainWindow
import sys
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QMessageBox
import form

class Autz(QtWidgets.QMainWindow, form.Ui_main):
    def __init__(self):
        super(Autz, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Autz()
    widget.show()
    sys.exit(app.exec_())

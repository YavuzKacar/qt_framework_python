from PyQt5 import QtWidgets

from mydesign import Ui_MainWindow

import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnCount(2)

        self.ui.tableWidget.setRowCount(4)


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
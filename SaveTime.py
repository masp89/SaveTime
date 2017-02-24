# Save Time for McDonald's Service Desk Sweden
# Written by Maria Aspvik at Capgemini Sweden.

import sys
from PyQt4 import  QtCore, QtGui

class Window(QtGui.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Spara Tid för McDonald's Servicedesk")
        self.setGeometry(500, 300, 500, 300)
        self.setWindowIcon(QtGui.QIcon("Happy-Hamburger.png"))
        self.home()

    def home(self):
        btn_quit = QtGui.QPushButton("Avsluta", self)
        btn_set = QtGui.QPushButton("Öppna Waystation", self)
        btn_quit.resize(125, 30)
        btn_set.resize(125, 30)
        btn_quit.move(275, 250)
        btn_set.move(100, 250)

        btn_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
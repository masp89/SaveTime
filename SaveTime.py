# Save Time for McDonald's Service Desk Sweden
# Written by Maria Aspvik at Capgemini Sweden.

import sys, subprocess
from PyQt4 import QtCore, QtGui

class Window(QtGui.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Spara Tid för McDonald's Servicedesk")
        self.setGeometry(500, 300, 500, 300)
        self.setWindowIcon(QtGui.QIcon("Happy-Hamburger.png"))
        self.home()

    def home(self):

        beskr = QtGui.QLabel("Ange restaurangnummer nedan.", self)
        beskr.resize(200,30)
        beskr.move(150,100)

        self.rest_nr = QtGui.QLineEdit("###", self)
        self.rest_nr.setMaxLength(3)
        self.rest_nr.resize(50, 30)
        self.rest_nr.move(225, 150)



        btn_quit = QtGui.QPushButton("Avsluta", self)
        btn_set = QtGui.QPushButton("Öppna Waystation", self)
        btn_quit.resize(125, 30)
        btn_set.resize(125, 30)
        btn_quit.move(275, 250)
        btn_set.move(100, 250)



        btn_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn_set.clicked.connect(self.WSconnect)

        self.show()

    def show_int_error(self):
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Information)
        message.setText("Skriv bara in siffror!")
        message.setWindowTitle("Fel!")
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.exec_()

    def WSconnect(self):
        try:
            val = int(self.rest_nr.text())
        except:
            self.show_int_error()

        if int(self.rest_nr.text()) == 231:
            ip = '*.*.' + self.rest_nr.text() + '.*'
            psw = '******'

        elif int(self.rest_nr.text()) < 256:
            ip = '*.*.' + self.rest_nr.text() + '.*'
            psw = '******'

        elif int(self.rest_nr.text()) > 256:
            temp_rest_nr = int(self.rest_nr.text()) - 256
            ip = '*.*.' + str(temp_rest_nr) + '.*'
            psw = '******'

        net_use_string = r'net use \\\\' + ip + '\\d$\\Newpos61 /user:Administrator ' + psw
        catalog_string = r'start \\\\' + ip + '\\d$\\Newpos61'
        wayweb_string = r'start iexplore.exe http://' + ip + ':8080/way.html'
        subprocess.Popen(net_use_string, shell=False)
        subprocess.Popen(wayweb_string, shell=False)
        subprocess.Popen(catalog_string, shell=False)




def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

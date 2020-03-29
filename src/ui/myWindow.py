# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.llave1 = QtWidgets.QCheckBox(self.centralwidget)
        self.llave1.setGeometry(QtCore.QRect(300, 250, 21, 20))
        self.llave1.setText("")
        self.llave1.setObjectName("llave1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -1, 991, 541))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Pictures/capturas de pantalla/tp1_assd/tp1_assd0000.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.llave2 = QtWidgets.QCheckBox(self.centralwidget)
        self.llave2.setGeometry(QtCore.QRect(450, 250, 21, 20))
        self.llave2.setText("")
        self.llave2.setObjectName("llave2")
        self.llave3 = QtWidgets.QCheckBox(self.centralwidget)
        self.llave3.setGeometry(QtCore.QRect(660, 250, 21, 20))
        self.llave3.setText("")
        self.llave3.setObjectName("llave3")
        self.llave4 = QtWidgets.QCheckBox(self.centralwidget)
        self.llave4.setGeometry(QtCore.QRect(870, 250, 21, 20))
        self.llave4.setText("")
        self.llave4.setObjectName("llave4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 280, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 280, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(830, 280, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(260, 280, 93, 28))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(10, 270, 93, 28))
        self.pushButton_input.setObjectName("pushButton_input")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(270, 50, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.label.raise_()
        self.llave3.raise_()
        self.llave2.raise_()
        self.llave4.raise_()
        self.llave1.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_input.raise_()
        self.titulo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Principal"))
        self.pushButton_2.setText(_translate("MainWindow", "Plot"))
        self.pushButton_3.setText(_translate("MainWindow", "Plot"))
        self.pushButton_4.setText(_translate("MainWindow", "Plot"))
        self.pushButton_1.setText(_translate("MainWindow", "Plot"))
        self.pushButton_input.setText(_translate("MainWindow", "Input"))
        self.titulo.setText(_translate("MainWindow", "Simulador de Circuitos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


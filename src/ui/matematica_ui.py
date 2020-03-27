# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matematica.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        self.titulo = QtWidgets.QLabel(Form)
        self.titulo.setGeometry(QtCore.QRect(20, 10, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.sub_titulo_1 = QtWidgets.QLabel(Form)
        self.sub_titulo_1.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.sub_titulo_1.setObjectName("sub_titulo_1")
        self.sub_titulo_2 = QtWidgets.QLabel(Form)
        self.sub_titulo_2.setGeometry(QtCore.QRect(20, 320, 121, 16))
        self.sub_titulo_2.setObjectName("sub_titulo_2")
        self.boton_cerrar = QtWidgets.QPushButton(Form)
        self.boton_cerrar.setGeometry(QtCore.QRect(380, 550, 93, 28))
        self.boton_cerrar.setObjectName("boton_cerrar")
        self.boton_guardar = QtWidgets.QPushButton(Form)
        self.boton_guardar.setGeometry(QtCore.QRect(260, 550, 93, 28))
        self.boton_guardar.setObjectName("boton_guardar")
        self.plotter_container = QtWidgets.QStackedWidget(Form)
        self.plotter_container.setGeometry(QtCore.QRect(30, 90, 441, 192))
        self.plotter_container.setObjectName("plotter_container")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.plotter_container.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.plotter_container.addWidget(self.page_2)
        self.plotter_container2 = QtWidgets.QStackedWidget(Form)
        self.plotter_container2.setGeometry(QtCore.QRect(30, 350, 441, 192))
        self.plotter_container2.setObjectName("plotter_container2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.plotter_container2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.plotter_container2.addWidget(self.page_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventana Grafica"))
        self.titulo.setText(_translate("Form", "SEÑAL DE SALIDA"))
        self.sub_titulo_1.setText(_translate("Form", "Señal en el tiempo"))
        self.sub_titulo_2.setText(_translate("Form", "Señal en frecuencia"))
        self.boton_cerrar.setText(_translate("Form", "Cerrar"))
        self.boton_guardar.setText(_translate("Form", "Guardar"))


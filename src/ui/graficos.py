# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficos.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 700)
        self.titulo = QtWidgets.QLabel(Form)
        self.titulo.setGeometry(QtCore.QRect(20, 10, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.sub_titulo_1 = QtWidgets.QLabel(Form)
        self.sub_titulo_1.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.sub_titulo_1.setObjectName("sub_titulo_1")
        self.sub_titulo_2 = QtWidgets.QLabel(Form)
        self.sub_titulo_2.setGeometry(QtCore.QRect(20, 350, 121, 16))
        self.sub_titulo_2.setObjectName("sub_titulo_2")
        self.boton_cerrar = QtWidgets.QPushButton(Form)
        self.boton_cerrar.setGeometry(QtCore.QRect(380, 650, 93, 28))
        self.boton_cerrar.setObjectName("boton_cerrar")
        self.plotter_container = QtWidgets.QStackedWidget(Form)
        self.plotter_container.setGeometry(QtCore.QRect(30, 110, 441, 192))
        self.plotter_container.setObjectName("plotter_container")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.plotter_container.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.plotter_container.addWidget(self.page_2)
        self.plotter_container2 = QtWidgets.QStackedWidget(Form)
        self.plotter_container2.setGeometry(QtCore.QRect(30, 380, 441, 192))
        self.plotter_container2.setObjectName("plotter_container2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.plotter_container2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.plotter_container2.addWidget(self.page_4)
        self.pushButton_borrar = QtWidgets.QPushButton(Form)
        self.pushButton_borrar.setGeometry(QtCore.QRect(270, 650, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_borrar.sizePolicy().hasHeightForWidth())
        self.pushButton_borrar.setSizePolicy(sizePolicy)
        self.pushButton_borrar.setObjectName("pushButton_borrar")
        self.label_auxiliar = QtWidgets.QLabel(Form)
        self.label_auxiliar.setGeometry(QtCore.QRect(24, 620, 461, 61))
        self.label_auxiliar.setText("")
        self.label_auxiliar.setObjectName("label_auxiliar")
        self.label_auxiliar2 = QtWidgets.QLabel(Form)
        self.label_auxiliar2.setGeometry(QtCore.QRect(0, 580, 481, 41))
        self.label_auxiliar2.setText("")
        self.label_auxiliar2.setObjectName("label_auxiliar2")
        self.label_auxiliar.raise_()
        self.titulo.raise_()
        self.sub_titulo_1.raise_()
        self.sub_titulo_2.raise_()
        self.boton_cerrar.raise_()
        self.plotter_container.raise_()
        self.plotter_container2.raise_()
        self.pushButton_borrar.raise_()
        self.label_auxiliar2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventana Grafica"))
        self.titulo.setText(_translate("Form", "SEÑAL DE SALIDA"))
        self.sub_titulo_1.setText(_translate("Form", "Señal en el tiempo"))
        self.sub_titulo_2.setText(_translate("Form", "Señal en frecuencia"))
        self.boton_cerrar.setText(_translate("Form", "Cerrar y Borrar"))
        self.pushButton_borrar.setText(_translate("Form", "Borrar"))


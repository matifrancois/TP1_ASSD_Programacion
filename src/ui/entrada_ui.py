# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrada.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 599)
        self.titulo = QtWidgets.QLabel(Dialog)
        self.titulo.setGeometry(QtCore.QRect(20, 20, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.subtitulo = QtWidgets.QLabel(Dialog)
        self.subtitulo.setGeometry(QtCore.QRect(20, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subtitulo.setFont(font)
        self.subtitulo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.subtitulo.setObjectName("subtitulo")
        self.subtitulo_2 = QtWidgets.QLabel(Dialog)
        self.subtitulo_2.setGeometry(QtCore.QRect(30, 380, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subtitulo_2.setFont(font)
        self.subtitulo_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.subtitulo_2.setObjectName("subtitulo_2")
        self.checkBox_senoidal_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_senoidal_2.setGeometry(QtCore.QRect(40, 430, 81, 20))
        self.checkBox_senoidal_2.setObjectName("checkBox_senoidal_2")
        self.checkBox_senoidal_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_senoidal_3.setGeometry(QtCore.QRect(40, 460, 81, 20))
        self.checkBox_senoidal_3.setObjectName("checkBox_senoidal_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 110, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 150, 211, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_amplitud = QtWidgets.QLabel(self.widget)
        self.label_amplitud.setObjectName("label_amplitud")
        self.gridLayout.addWidget(self.label_amplitud, 0, 0, 1, 1)
        self.lineEdit_amplitud = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_amplitud.setObjectName("lineEdit_amplitud")
        self.gridLayout.addWidget(self.lineEdit_amplitud, 0, 1, 1, 1)
        self.label_frecuencia = QtWidgets.QLabel(self.widget)
        self.label_frecuencia.setObjectName("label_frecuencia")
        self.gridLayout.addWidget(self.label_frecuencia, 1, 0, 1, 1)
        self.lineEdit_frecuencia = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_frecuencia.setObjectName("lineEdit_frecuencia")
        self.gridLayout.addWidget(self.lineEdit_frecuencia, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titulo.setText(_translate("Dialog", "SEÑAL DE ENTRADA"))
        self.subtitulo.setText(_translate("Dialog", "Introduzca la señal deseada"))
        self.subtitulo_2.setText(_translate("Dialog", "Introduzca el tipo de muestreo deseado"))
        self.checkBox_senoidal_2.setText(_translate("Dialog", "Tiempo "))
        self.checkBox_senoidal_3.setText(_translate("Dialog", "Senoidal"))
        self.comboBox.setItemText(0, _translate("Dialog", "Senoidal"))
        self.comboBox.setItemText(1, _translate("Dialog", "Cuadratica"))
        self.comboBox.setItemText(2, _translate("Dialog", "3/2 Senoidal"))
        self.label_amplitud.setText(_translate("Dialog", "Amplitud"))
        self.label_frecuencia.setText(_translate("Dialog", "Frecuencia"))


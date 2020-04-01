from src.ui.ventanaEntrada import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QDialog, QComboBox, QApplication
from src.app import *
import sys

class Ventana_Entrada(QDialog, Ui_Dialog):
    """ Creamos nuestra clase Ventana_Entrada, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """

    def __init__(self):
        super(QDialog, self).__init__()        # Llamamos al constructor de los padres
        self.setupUi(self)
        self.comboBox_senial.currentIndexChanged.connect(self.cambie_de_eleccion)
        self.frecuencia = ""
        self.senial_elegida = ""
        self.amplitud = ""
        self.inicio_rango = ""
        self.fin_rango = ""
        self.tau = ""
        self.T = ""
        self.muestreo_elegido = ""
        self.almacenamiento = 0.0
        self.x = 0
        self.amplitud_am = ""
        self.frecuencia_am = ""
        self.coeficiente = ""
        self.lineEdit_amplitud_moduladora.setDisabled(True)
        self.lineEdit_frecuencia_moduladora.setDisabled(True)
        self.lineEdit_coeficiente.setDisabled(True)

    def getItem(self, x):
        self.senial_elegida = self.comboBox_senial.currentText()
        self.amplitud = self.lineEdit_amplitud.text()
        self.frecuencia = self.lineEdit_frecuencia.text()
        self.tau = self.lineEdit_tao.text()
        self.T = self.lineEdit_t.text()
        self.muestreo_elegido = self.comboBox_tipo_muestreo.currentText()
        self.inicio_rango = self.lineEdit_inicio_rango.text()
        self.fin_rango = self.lineEdit_fin_rango.text()
        self.amplitud_am = self.lineEdit_amplitud_moduladora.text()
        self.frecuencia_am = self.lineEdit_frecuencia_moduladora.text()
        self.coeficiente = self.lineEdit_coeficiente.text()
        if self.muestreo_elegido == "Natural":
            return self.muestreo_natural(x)
        elif self.muestreo_elegido == "Instantaneo":
            return self.muestreo_instantaneo(x)
        else:
            return self.muestreo_independiente()


    def muestreo_natural(self, x):
        """
        se encarga de que se apaguen los checkbox no utilizados
        :return:
        """
        self.x = x
        print(self.x)
        self.almacenamiento = 0.0
        if self.x % 10 == 1:
            self.almacenamiento -= 1.0
        if (int((self.x/10)) % 10) == 1:
            self.almacenamiento -= 10.0
        if (int((self.x/100)) % 10) == 1:
            self.almacenamiento -= 100.0
        if (int((self.x/1000)) % 10) == 1:
            self.almacenamiento -= 1000.0
        print(self.almacenamiento)
        return self.almacenamiento

    def muestreo_instantaneo(self, x):
        """
        se encarga de que se apaguen los checkbox no utilizados
        :return:
        """
        self.x = x
        self.almacenamiento = 0.0
        if self.x % 10 == 1:
            self.almacenamiento -= 1.0
        if (int((self.x / 10)) % 10) == 0:
            self.almacenamiento += 10.0
        if (int((self.x / 100)) % 10) == 0:
            self.almacenamiento += 100.0
        if (int((self.x / 1000)) % 10) == 1:
            self.almacenamiento -= 1000.0
        return self.almacenamiento

    def muestreo_independiente(self):
        """
        se encarga de que se apaguen los checkbox no utilizados
        :return:
        """
        return 0



    def cambie_de_eleccion(self):
        """
        funcion que se encarga de inhabilitar la entrada de datos en las situaciones requeridas
        :return:
        """
        if self.comboBox_senial.currentText() == "AM":
            self.lineEdit_amplitud_moduladora.setDisabled(False)
            self.lineEdit_frecuencia_moduladora.setDisabled(False)
            self.lineEdit_coeficiente.setDisabled(False)
        else:
            self.lineEdit_amplitud_moduladora.setDisabled(True)
            self.lineEdit_frecuencia_moduladora.setDisabled(True)
            self.lineEdit_coeficiente.setDisabled(True)

from src.ui.myWindow import *
from src.ui.ventanaEntrada import *
from PyQt5.QtWidgets import QWidget, QDialog, QComboBox
from src.ventanaEntrada import Ventana_Entrada
from src.graficos import MatplotlibWidget
from src.app import *


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self,  Backend, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.x = 0
        self.label.setPixmap(QtGui.QPixmap('assets\\tp1_assd' + str(self.x) + '.jpg'))
        self.llave1.pressed.connect(lambda: self.cambia(1000, not self.llave1.isChecked()))  # seteamos el callback para cada que toquen la checkBox
        self.llave2.pressed.connect(lambda: self.cambia(100, not self.llave2.isChecked()))  # seteamos el callback para cada que presione la checkBox
        self.llave3.pressed.connect(lambda: self.cambia(10, not self.llave3.isChecked()))  # seteamos el callback para cada que presionen la checkBox
        self.llave4.pressed.connect(lambda: self.cambia(1, not self.llave4.isChecked()))  # seteamos el callback para cada que presionen la checkBox
        self.pushButton_1.clicked.connect(self.graficando)
        self.pushButton_input.clicked.connect(self.input)
        self.objetoEntrada = Ventana_Entrada()
        self.widgetGrafico = MatplotlibWidget()

        # self.muestreo_natural_activado() #esto es para cuando el muestreo natural se haya activado

    """def muestreo_natural_activado(self):
        global x
        x=x
        self.llave2.setChecked(False)
        self.llave2.setEnabled(False)
        self.llave3.setChecked(False)
        self.llave3.setEnabled(False)
        self.muestra_fondo()
    """

    def cambia(self, constante, booleano):
        """
        Esta funcion se encarga de segun qué llave esta activada sumar qué valor al numero x para asi referenciar
        facilmente a los archivos imagenes
        :param constante:
        :param booleano:
        :return:
        """
        if booleano:
            self.x += constante
        else:
            self.x -= constante
        self.muestra_fondo()

    def muestra_fondo(self):
        """
        Esta funcion se encarga de mostrar en pantalla la imagen segun el nuemero x
        :return:
        """
        self.label.setPixmap(QtGui.QPixmap('assets\\tp1_assd' + str(self.x) + '.jpg'))

    def graficando(self):
        """
        Esta funcion muestra el widget
        :return:
        """
        self.widgetGrafico.show()

    def input(self):
        """
        Muestra el objeto entrada
        :return:
        """
        self.objetoEntrada.show()


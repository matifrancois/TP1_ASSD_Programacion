from src.ui.myWindow import *
from src.ui.ventanaEntrada import *
from PyQt5.QtWidgets import QWidget, QDialog, QComboBox
from src.ventanaEntrada import Ventana_Entrada
from src.graficos import MatplotlibWidget
from src.app import *


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self,  backend, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        """
        -> x es la variable encargada de guardar un numero entero donde cada digito puede valer 0 o 1 
        ejemplo: 1011 indica que la ficha 1, 3 y 4 estan activadas (respecto de la foto original del tp)
        -> almacenamiento es la varible que se utiliza como auxiliar para ver cuanto hay que sumarle a x (o restarle)
        para que luego de setear los valores que se requieran segun el modo de sampleo te devuelva x como lo necesites
        
        
        """
        self.x = 0
        self.almacenamiento = 0
        self.backend = backend
        self.label.setPixmap(QtGui.QPixmap('assets\\fotos_fondo\\tp1_assd' + str(int(self.x)) + '.jpg'))
        self.llave1.pressed.connect(lambda: self.cambia(1000, not self.llave1.isChecked()))  # seteamos el callback para cada que toquen la checkBox
        self.llave2.pressed.connect(lambda: self.cambia(100, not self.llave2.isChecked()))  # seteamos el callback para cada que presione la checkBox
        self.llave3.pressed.connect(lambda: self.cambia(10, not self.llave3.isChecked()))  # seteamos el callback para cada que presionen la checkBox
        self.llave4.pressed.connect(lambda: self.cambia(1, not self.llave4.isChecked()))  # seteamos el callback para cada que presionen la checkBox
        self.pushButton_1.clicked.connect(lambda: self.graficando(1, self.backend))
        self.pushButton_2.clicked.connect(lambda: self.graficando(2, self.backend))
        self.pushButton_3.clicked.connect(lambda: self.graficando(3, self.backend))
        self.pushButton_4.clicked.connect(lambda: self.graficando(4, self.backend))
        self.pushButton_input.clicked.connect(self.input)
        self.objetoEntrada = Ventana_Entrada()
        self.widgetGrafico = MatplotlibWidget()

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
        self.label.setPixmap(QtGui.QPixmap('assets\\fotos_fondo\\tp1_assd' + str(int(self.x)) + '.jpg'))

    def graficando(self, nodo, backend):
        """
        Esta funcion muestra el widget
        :return:
        """
        self.widgetGrafico.move(1400, 80)
        self.widgetGrafico.show()
        self.widgetGrafico.on_plot_update(nodo, self.comboBox_senial_a_graficar.currentText(), backend)

    def input(self):
        """
        Muestra el objeto entrada
        :return:
        """
        if self.objetoEntrada.exec():
            self.almacenamiento = self.objetoEntrada.getItem(self.x)
            self.x += self.almacenamiento
            self.seteando_fichas()
            self.label.setPixmap(QtGui.QPixmap('assets\\fotos_fondo\\tp1_assd' + str(int(self.x)) + '.jpg'))
            self.backend.set_input({'senial_elegida': self.objetoEntrada.senial_elegida,
                                    'amplitud': self.objetoEntrada.amplitud,
                                    'frecuencia': self.objetoEntrada.frecuencia,
                                    'llaves': self.x,
                                    'tau': self.objetoEntrada.tau,
                                    'T': self.objetoEntrada.T})
            self.comboBox_senial_a_graficar.addItem(self.objetoEntrada.senial_elegida +
                                                    " A:" + self.objetoEntrada.amplitud +
                                                    " f:" + self.objetoEntrada.frecuencia +
                                                    " tau" + self.objetoEntrada.tau +
                                                    " t" + self.objetoEntrada.T)

    def seteando_fichas(self):
        if self.x % 10 == 1:
            self.llave4.setChecked(True)
        else:
            self.llave4.setChecked(False)
        if (int((self.x / 10)) % 10) == 1:
            self.llave3.setChecked(True)
        else:
            self.llave3.setChecked(False)
        if (int((self.x / 100)) % 10) == 1:
            self.llave2.setChecked(True)
        else:
            self.llave2.setChecked(False)
        if (int((self.x / 1000)) % 10) == 1:
            self.llave1.setChecked(True)
        else:
            self.llave1.setChecked(False)

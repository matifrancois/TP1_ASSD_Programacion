# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QDialog, QComboBox
from PyQt5.Qt import pyqtSlot

# Python modules
import sys

# Matplotlib Modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Project Modules
from src.ui.matematica_ui import Ui_Form
from src.ui.grafiquitos_ui import *
from src.ui.entrada_ui import *

# Python Modules
from numpy import *
from time import *
from random import *

x=0

def main():
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label.setPixmap(QtGui.QPixmap('assets\\tp1_assd' + str(x) + '.jpg'))
        self.llave1.pressed.connect(self.cambia_llave_1)  # seteamos el calback para cada vez que apreten la checkBox
        self.llave2.pressed.connect(self.cambia_llave_2)  # seteamos el calback para cada vez que apreten la checkBox
        self.llave3.pressed.connect(self.cambia_llave_3)  # seteamos el calback para cada vez que apreten la checkBox
        self.llave4.pressed.connect(self.cambia_llave_4)  # seteamos el calback para cada vez que apreten la checkBox
        self.pushButton_1.clicked.connect(self.mat_1)
        self.pushButton_1.clicked.connect(self.mat_1)
        self.pushButton_input.clicked.connect(self.input)
        #self.muestreo_natural_activado() #esto es para cuando el muestreo natural se haya activado

    """def muestreo_natural_activado(self):
        global x
        x=x
        self.llave2.setChecked(False)
        self.llave2.setEnabled(False)
        self.llave3.setChecked(False)
        self.llave3.setEnabled(False)
        self.muestra_fondo()
    """

    def cambia_llave_1(self):
        global x
        if not self.llave1.isChecked():
            x += 1000
        else:
            x -= 1000
        self.muestra_fondo()

    def cambia_llave_2(self):
        global x
        if not self.llave2.isChecked():
            x += 100
        else:
            x -= 100
        self.muestra_fondo()

    def cambia_llave_3(self):
        global x
        if not self.llave3.isChecked():
            x += 10
        else:
            x -= 10
        self.muestra_fondo()

    def cambia_llave_4(self):
        global x
        if not self.llave4.isChecked():
            x += 1
        else:
            x -= 1
        self.muestra_fondo()

    def muestra_fondo(self):
        self.label.setPixmap(QtGui.QPixmap('assets\\tp1_assd' + str(x) + '.jpg'))

    def mat_1(self):
        self.widget = MatplotlibWidget()  #todo por que aca tiene que ser self y sin self se cerraba???
        self.widget.show()

    def input(self):
            self.ventana_entrada = Ventana_Entrada()  # todo por que aca tiene que ser self y sin self se cerraba???
            self.ventana_entrada.mostrar()




class   Ventana_Entrada(QWidget, Ui_Dialog):
    """ Creamos nuestra clase Ventana_Entrada, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """

    def __init__(self):
        super(Ventana_Entrada, self).__init__()        # Llamamos al constructor de los padres
        self.setupUi(self)
        self.comboBox_senial.currentIndexChanged.connect(self.cambie_de_eleccion)
        self.comboBox_tipo_muestreo.currentIndexChanged.connect(self.cambie_de_eleccion_2)
        self.pushButton_ok.clicked.connect(self.getItem)
        self.frecuencia=0
        self.analisis = dateando()

    def cambie_de_eleccion(self):
        self.senial_elegida = self.comboBox_senial.currentText()
        if self.senial_elegida == "Cuadratica":
            self.lineEdit_frecuencia.setDisabled(True)
        else:
            self.lineEdit_frecuencia.setDisabled(False)

    def cambie_de_eleccion_2(self):
        self.muestreo_elegido = self.comboBox_tipo_muestreo.currentText()
        if self.muestreo_elegido == "Muestreo Instantaneo":
            self.lineEdit_tao.setDisabled(True)
        else:
            self.lineEdit_tao.setDisabled(False)

    def getItem(self):
        self.senial_elegida = self.comboBox_senial.currentText()
        self.amplitud = self.lineEdit_amplitud.text()
        self.frecuencia = self.lineEdit_frecuencia.text()
        self.muestreo_elegido = self.comboBox_tipo_muestreo.currentText()
        self.tao = self.lineEdit_tao.text()
        self.tiempo = self.lineEdit_t.text()
        self.analisis.frecuencia_text = self.frecuencia
        self.analisis.amplitud_text = self.amplitud
        self.analisis.senial= self.senial_elegida
        self.analisis.mostrar_dato()
        self.close()

    def mostrar(self):
        self.show()


class   MatplotlibWidget(QWidget, Ui_Form):
    """ Creamos nuestra clase MatplotlibWidget, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """

    def __init__(self):
        super(MatplotlibWidget, self).__init__()        # Llamamos al constructor de los padres
        self.setupUi(self)


        # Tenemos que utilizar el backend que provee Matplotlib para PyQt y crear un FigureCanvas,
        # son las entidades encargadas de proveer el soporte grafico necesario para dibujar en pantalla
        # y basicamente hacen la magica.
        #
        # Asi como FigureCanvas es el control del entorno grafico donde dibujamos, Figure
        # corresponde al espacio utilizado para dibujar y despues sobre el se agregan pares de ejes.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)

        # A partir de aca es lo mismo que con pyplot, solo que el manejo no es automatico, sino
        # que lo hace uno con criterio, entonces creamos un par de ejes
        self.axes = self.figure.add_subplot()
        self.axes2 = self.figure2.add_subplot()

        # IMPORTANTE! FigureCanvas es un Widget, pero nunca dijimos que lo muestre! Para eso voy a usar
        # una forma comoda, con QStackedWidget... agregamos una pagina donde esta FigureCanvas y la configuramos
        # como la actual
        canvas_index = self.plotter_container.addWidget(self.canvas)
        self.plotter_container.setCurrentIndex(canvas_index)
        canvas_index2 = self.plotter_container2.addWidget(self.canvas2)
        self.plotter_container2.setCurrentIndex(canvas_index2)

        # Algo mas emocionante, cambiemos el contenido con un callback al boton de pantalla!
        self.on_plot_update()

    @pyqtSlot()
    def on_plot_update(self):
        """ Slot/Callback usado para actualizar datos en el Axes """

        # Creamos un puntos para el eje x y para el eje y!
        x_axis = linspace(0, 4 * pi, num=1000)
        y_axis = sin( 2*x_axis )
        x_axis2 = linspace(0, 4 * pi, num=1000)
        y_axis2 = sin(4 * x_axis)


        #plt.plot(x_axis,y_axis)
        #plt.show()

        # Limpiamos el axes, agregamos los puntos, y actualizamos el canvas
        # IMPORTANTE! Te invito a comentar para que veas la importancia del .clear() y .draw()
        #self.axes.clear()
        self.axes.plot(x_axis, y_axis)
        self.canvas.draw()

        #self.axes2.clear()
        self.axes2.plot(x_axis2, y_axis2)
        self.canvas2.draw()

#TODO organizar las 4 funciones para que queden en una y sacar la variable global de ahi creandola en def init para luego pasarla por referencia a la funcion antes dicha
#TODO falta tambien darle funcionalidad a los botones de la ventana grafica y permitirle elegir diferentes entradas de señal.
#TODO falta que se pueda calcular la transformada rapida de fourier con fft
#TODO falta hacerlo como lo hizo pablo y no lucas

class   dateando():
    """ Creamos nuestra clase MatplotlibWidget, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """

    def __init__(self):
        super(dateando, self).__init__()        # Llamamos al constructor de los padres
        #self.setupUi(self)# Necesitamos usar esto para hacer el build de los componentes
        self.senial = ""
        self.frecuencia_text = ""
        self.amplitud_text = ""
        self.frecuencia =0



    def mostrar_dato(self):
        print(self.senial)
        print(self.amplitud_text)
        if self.frecuencia_text.isdigit():
            self.frecuencia = float(self.frecuencia_text) +20
            print(self.frecuencia)
        else:
            print("frecuencia invalida")
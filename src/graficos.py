from src.ui.graficos import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import pyqtSlot
from PyQt5 import QtGui
# Matplotlib Modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

# Python Modules
from numpy import *
from time import *
from random import *



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
        self.toolbar = NavigationToolbar(self.canvas, self)  # cada gráfico tiene un toolbar con herramientos para


        # trabajar sobre él
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
        self.axes.plot(x_axis, y_axis, label="Señal")
        self.canvas.draw()
        #self.axes2.clear()
        self.axes2.plot(x_axis2, y_axis2, label="Señal")
        self.canvas2.draw()
        # Configuramos los ejes para que tengan un label
        self.axes.set_xlabel("Time [s]")
        self.axes.set_ylabel("Voltage [V]")
        self.axes2.set_xlabel("frecuencia [Hz]")
        self.axes2.set_ylabel("FFT")
        #para mostrar la leyenda
        self.figure.legend()
        self.figure2.legend()
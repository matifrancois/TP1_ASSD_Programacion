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
        super(QWidget, self).__init__()        # Llamamos al constructor de los padres
        self.setupUi(self)

        # Tenemos que utilizar el backend que provee Matplotlib para PyQt y crear un FigureCanvas,
        # son las entidades encargadas de proveer el soporte grafico necesario para dibujar en pantalla
        # y basicamente hacen la magica.
        #
        # Asi como FigureCanvas es el control del entorno grafico donde dibujamos, Figure
        # corresponde al espacio utilizado para dibujar y despues sobre el se agregan pares de ejes.
        self.figure = Figure()
        # La siguiente linea se encarga de ajustar los valores por def de la ventana para que se vean bien
        self.figure.subplots_adjust(left=0.127, bottom=0.234, right=0.981, top=0.921, wspace=0.2, hspace=0.2)
        self.canvas = FigureCanvas(self.figure)
        self.figure2 = Figure()
        # La siguiente linea se encarga de ajustar los valores por def de la ventana para que se vean bien
        self.figure2.subplots_adjust(left=0.127, bottom=0.234, right=0.981, top=0.921, wspace=0.2, hspace=0.2)
        self.canvas2 = FigureCanvas(self.figure2)
        # cada gráfico tiene un toolbar con herramientos para trabajar sobre él
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.boton_cerrar.clicked.connect(self.cerrar)
        self.pushButton_borrar.clicked.connect(self.borrar)


        self.figure.legend()
        self.figure2.legend()

        # TODO revisar para que la barra de tareas no quede arriba de los graficos
        ###########################################################################

        self.grid = QGridLayout()
        self.grid.addWidget(self.titulo, 1, 0)
        self.grid.addWidget(self.sub_titulo_1, 2, 0)
        self.grid.addWidget(self.plotter_container, 3, 0)  # Se le agrega el canvas al widget
        self.grid.addWidget(self.toolbar, 4, 0)
        self.grid.addWidget(self.sub_titulo_2, 5, 0)
        self.grid.addWidget(self.plotter_container2, 6, 0)  # Se le agrega el canvas al widget
        self.grid.addWidget(self.toolbar2, 7, 0)
        self.grid.addWidget(self.label_auxiliar, 8, 0)
        self.grid.addWidget(self.label_auxiliar2, 9, 0)

        #self.grid.addWidget(self.pushButton_borrar, 5, 0)  # Se le agrega el canvas al widget
        #self.grid.addWidget(self.boton_cerrar, 5, 1)  # Se le agrega el canvas al widget


        self.setLayout(self.grid)

        ###########################################################################

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
        #self.on_plot_update()

    @pyqtSlot()
    def on_plot_update(self, nodo, senial_a_graficar, backend, x):
        """ Slot/Callback usado para actualizar datos en el Axes """

        backend.emulateCircuit(x, senial_a_graficar)
        # buscamos los datos del backend, 2 refiere al de la frecuencia!
        self.x_axis, self.y_axis = backend.getNode(nodo)
        self.x_axis2, self.y_axis2 = backend.fourierTransform(nodo)
        # Limpiamos el axes, agregamos los puntos, y actualizamos el canvas
        # IMPORTANTE! Te invito a comentar para que veas la importancia del .clear() y .draw()

        self.axes.set_xlabel("Time [s]")
        self.axes.set_ylabel("Voltage [V]")
        self.axes2.set_xlabel("frecuencia [Hz]")
        self.axes2.set_ylabel("FFT")



        #self.axes.clear()
        self.axes.plot(self.x_axis, self.y_axis, label="Señal")
        self.axes2.plot(self.x_axis2, abs(self.y_axis2), label="Señal2")
        # para mostrar la leyenda TODO (esto estaria bueno para ponerle que nodo es
        self.legend = self.figure.legend()
        self. legend2 = self.figure2.legend()
        self.canvas.draw()
        #self.axes2.clear()
        self.canvas2.draw()
        # Configuramos los ejes para que tengan un label




    def cerrar(self):
        self.borrar()
        self.close()

    # ver por que no se borran los legend
    def borrar(self):
        #self.legend.remove()
        #self.legend2.remove()
        self.axes.clear()
        self.axes2.clear()
        self.canvas.draw()
        self.canvas2.draw()


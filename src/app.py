# Python modules
import sys

# Project Modules
from src.ui.myWindow import *
from src.myWindow import MyWindow
from src.backend import backend


# Python Modules
from numpy import *


def main():
    app = QtWidgets.QApplication([])
    Backend = backend()
    window = MyWindow(Backend)
    window.show()
    sys.exit(app.exec_())








#TODO organizar las 4 funciones para que queden en una y sacar la variable global de ahi creandola en def init para luego pasarla por referencia a la funcion antes dicha
#TODO falta tambien darle funcionalidad a los botones de la ventana grafica y permitirle elegir diferentes entradas de señal.
#TODO falta que se pueda calcular la transformada rapida de fourier con fft
#TODO falta hacerlo como lo hizo pablo y no lucas



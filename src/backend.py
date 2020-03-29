import scipy.signal as sps
import scipy as sp
import numpy as np
import matplotlib as mpl

# CONSTANTES
POINTS_ON_GRAPHIC = 1000
AAS_NUM = []
AAS_DEN = []
REC_NUM = []
REC_DEN = []

TIME = 0
VALUE = 1

NATURAL = 0
INSTANT = 1



class backend():
    """ Creamos nuestra clase MatplotlibWidget, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """
    def __init__(self):
        super(backend, self).__init__()        # Llamamos al constructor de los padres
        # self.setupUi(self)# Necesitamos usar esto para hacer el build de los componentes
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


    # generateInput()
    # genera una lista de valores temporales de la señal de entrada del circuito
    def generateInput(self):

        return

    # emulateAAFilter()
    # emula el filtro anti-aliasing del circuito sobre un determinado arreglo
    def emulateAAFilter(self):

        return

    # emulateRecoveryFilter()
    # emula el filtro de recuperación del circuito sobre un determinado arreglo
    def emulateRecoveryFilter(self):

        return

    # emulateSampleNHold()
    # emula el sample & hold del circuito
    def emulateSampleNHold(self, type, source_signal, period, tau=0):
        if type == NATURAL:
            arr = self.naturalSample(source_signal,period,tau)
        else:
            arr = self.instantSample(source_signal,period)
        return arr

    # emulateAnalogSwitch()
    # emula la llave analógica del circuito
    def emulateAnalogSwitch(self):

        return

    # naturalSample()
    # simula el sampleo natural sobre una entrada determinada
    def naturalSample(self, source_signal, period, tau):
        arr = source_signal
        i = 0
        j = 0
        while i < len(arr[TIME]):
            if (arr[TIME][i] - arr[TIME][0]) < (j+1)*period:
                if (arr[TIME][i] - arr[TIME][0]) > (j*period + tau):
                    arr[VALUE][i] = 0   # fuera del pulso
                i += 1
            else:
                j += 1                         # si esta fuera de rango, incremento contador de periodos
        return arr

    # instantSample()
    # simula el sampleo instantáneo sobre una entrada determinada
    def instantSample(self, source_signal, period):
        arr = source_signal
        i = 1
        j = 1                                            # set en 1 dado que el primer valor del arreglo se considera muestreado
        while i < len(arr[TIME]):                        # para cada elemento del arreglo
            if (arr[TIME][i] - arr[TIME][0]) < j*period: # arr[TIME][0] representa el tiempo inicial
                arr[VALUE][i] = arr[VALUE][i-1]          # asigno valor anterior al actual
            else:
                j += 1                                   # incremento contador de períodos
            i += 1
        return arr
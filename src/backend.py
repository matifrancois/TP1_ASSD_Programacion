import scipy.signal as sps
import numpy as np
from copy import deepcopy

# CANTIDAD DE PUNTOS POR NODO
POINTS = 500000

# POLOS Y CEROS DE LOS FILTROS

POLES1 = [
    -35144-10601j,
    -35144+10601j
]

POLES2 = [
    -22315-22611j,
    -22315+22611j
]

POLES3 = [
    -11004-24975j,
    -11004+24975j
]

POLES4 = [
    -3260-24856j,
    -3260+24856j
]

ZEROS1 = [
    169084j,
    -169084j
]

ZEROS2 = [
    59374j,
    -59374j
]

ZEROS3 = [
    39672j,
    -39672j
]

ZEROS4 = [
    33632j,
    -33632j
]

GAIN = 0.00354787141836514

# CONSTANTES FUNCIONALES DEL PROGRAMA
TIME = 0
VALUE = 1


class Backend():
    """ Creamos nuestra clase MatplotlibWidget, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """
    def __init__(self):
        super(Backend, self).__init__()        # Llamamos al constructor de los padres
        #self.setupUi(self)# Necesitamos usar esto para hacer el build de los componentes
        self.signalType = ""
        self.amplitude = 0.0  # en el caso de AM, representa la de la moduladora
        self.frequency = 1.0  # en el caso de AM, representa la de la moduladora
        self.signalPeriod = 1 / self.frequency # en el caso de AM, representa la de la moduladora
        self.samplePeriod = 0.0
        self.tau = 0.0
        self.period_qty = 0

        # Párametros AM
        self.carrierAmplitude = 0.0
        self.carrierFrequency = 0.0
        self.modulationFactor = 0.0

        # Nodos del sistema
        self.nodes = [[np.zeros(POINTS), np.zeros(POINTS)], [np.zeros(POINTS), np.zeros(POINTS)], [np.zeros(POINTS), np.zeros(POINTS)], [np.zeros(POINTS), np.zeros(POINTS)], [np.zeros(POINTS), np.zeros(POINTS)]]

    def check_input(self, dic):
        """
        comprueba que los valores del diccionario tengan sentido sino devuelve un flag y el string con el comentario
        indicando por que no tuvo sentido
        :param diccionario:
        :return: flag (0 all bien o -1 all mal), string
        """
        err = [0] # inicializo error nulo
        if dic["type"] == "Senoidal" or dic["type"] == "3/2 Senoidal" or dic["type"] == "Cuadratica":
            if not dic["freq"].replace(".","1",1).isdigit() or float(dic["freq"]) <= 0:
                err[0] = -1
                err.append("La frecuencia de la señal debe ser no nula y positiva.")

            if not dic["amp"].replace(".","1",1).isdigit() or float(dic["amp"]) < 0:
                err[0] = -1
                err.append("La amplitud de la señal debe ser un número real positivo.")

        elif dic["type"] == "AM":
            if not dic["carrierFreq"].replace(".","1",1).isdigit() or float(dic["carrierFreq"]) <= 0:
                err[0] = -1
                err.append("La frecuencia de la señal portadora debe ser no nula y positiva.")

            if not dic["modulatingFreq"].replace(".","1",1).isdigit() or (float(dic["modulatingFreq"]) <= 0):
                err[0] = -1
                err.append("La frecuencia de la señal moduladora  debe ser no nula y positiva.")

            if not dic["carrierAmp"].replace(".","1",1).isdigit() or float(dic["carrierAmp"]) < 0:
                err[0] = -1
                err.append("La amplitud de la señal portadora debe ser un número real.")

            if not dic["modulatingAmp"].replace(".","1",1).isdigit() or float(dic["modulatingAmp"]) < 0:
                err[0] = -1
                err.append("La amplitud de la señal moduladora debe ser un número real.")

            if (not dic["modulationFactor"].replace(".","1",1).isdigit()) or float(dic["modulationFactor"]) > 1 or float(dic["modulationFactor"]) < 0:
                err[0] = -1
                err.append("El factor de modulación debe estar entre 0 y 1.")

        # Chequeos comunes a todas las señales

        if (not dic["samplePeriod"].replace(".","1",1).isdigit()) or (float(dic["samplePeriod"]) <= 0):
            err[0] = -1
            err.append("El periodo de muestreo debe ser un número real no nulo.")

        if not dic["periodQty"].replace(".","1",1).isdigit() or (not float(dic["periodQty"]).is_integer()) or float(dic["periodQty"]) <= 0:
            err[0] = -1
            err.append("El número de periodos a graficar debe ser entero y positivo.")

        if (not dic["tau"].replace(".","1",1).isdigit()) or float(dic["tau"]) < 0:
            err[0] = -1
            err.append("Tau debe ser un número real positivo.")

        elif (not dic["samplePeriod"].replace(".","1",1).isdigit()) or (float(dic["tau"]) > float(dic["samplePeriod"])):
            err[0] = -1
            err.append("Tau no puede ser mayor que el período de muestreo")

        return err


#getNode()
#devuelve la información en tiempo del nodo indicado. DEVUELVE LA CANTIDAD DE PERIODOS A MOSTRAR
    def getNode(self, node_num):
        x = min(POINTS, int(POINTS * self.period_qty/5.0))  # si la cantidad de periodos a mostrar es inferior a 5, recorto el arreglo
        return self.nodes[node_num][TIME][0:x], self.nodes[node_num][VALUE][0:x]

    # parseString()
    # parser del string de comunicación con el frontend. Se asumen datos validados previamente
    # actualiza los datos del objeto
    def parseString(self, string):
        fields = string.split()  # tokenizacion del string
        self.signalType = fields[0]

        if self.signalType != 'AM':
            self.amplitude = float(fields[1].split(':')[1])
            self.frequency = float(fields[2].split(':')[1])
            self.samplePeriod = float(fields[3].split(':')[1])
            self.period_qty = float(fields[4].split(':')[1])
            self.tau = float(fields[5].split(':')[1])

        else:
            self.carrierAmplitude = float(fields[1].split(':')[1])
            self.carrierFrequency = float(fields[2].split(':')[1])
            self.amplitude = float(fields[3].split(':')[1])     # moduladora
            self.frequency = float(fields[4].split(':')[1])     # moduladora
            self.modulationFactor = float(fields[5].split(':')[1])
            self.samplePeriod = float(fields[6].split(':')[1])
            self.period_qty = float(fields[7].split(':')[1])
            self.tau = float(fields[8].split(':')[1])

        self.signalPeriod = 1.0/self.frequency
        return



    # emulateCircuit()
    # emula cada nodo del circuito para una determinada configuración.
    def emulateCircuit(self, circuitTopology, signal):
        self.parseString(signal)
        self.generateInput() # Genero señal de entrada (nodo 0)

        if (int(circuitTopology / 1000) % 10) == 1:
            self.nodes[1] = deepcopy(self.nodes[0])
        else:
            print("AAF activo")
            self.emulateAAFilter()

        if int(circuitTopology / 100) % 10 == 1:
            print("SH activo")
            self.emulateSampleNHold()
        else:
            self.nodes[2] = deepcopy(self.nodes[1])
        if int(circuitTopology / 10) % 10 == 1:
            self.nodes[3] = deepcopy(self.nodes[2])
        else:
            print("AnSwitch activo")
            self.emulateAnalogSwitch()

        if int(circuitTopology) % 10 == 1:
            self.nodes[4] = deepcopy(self.nodes[3])
        else:
            print("RF activo")
            self.emulateRecoveryFilter()

        return

    # generateinput()
    # genera el primer nodo del circuito, teniendo en cuenta los parametros de la señal que recibe del objeto
    def generateInput(self):

        nPeriod = max(5, self.period_qty) # Se establece un mínimo de 5 periodos para la fft. De todas formas, se grafica la cantidad de períodos elegida

        self.nodes[0][TIME] = np.linspace(0,nPeriod*self.signalPeriod, POINTS)  # creo eje temporal

        if self.signalType == "Senoidal":
            self.nodes[0][VALUE] = self.amplitude * np.sin(2 * np.pi * self.frequency * self.nodes[0][TIME])  # genero señal senoidal
        elif self.signalType == "Cuadratica":
            i = 0
            j = 0
            while i < len(self.nodes[0][TIME]):
                if self.nodes[0][TIME][i] < self.signalPeriod*(j+1):
                    if self.nodes[0][TIME][i] < (j+0.5)*self.signalPeriod:
                        self.nodes[0][VALUE][i] = self.amplitude * (self.nodes[0][TIME][i] - self.signalPeriod * j) ** 2
                    else:
                        self.nodes[0][VALUE][i] = self.amplitude * (self.signalPeriod*(j+1) - self.nodes[0][TIME][i]) ** 2
                    i += 1
                else:
                    j += 1
            return

        elif self.signalType == "AM":
            self.nodes[0][VALUE] = self.carrierAmplitude * (1+self.modulationFactor*self.amplitude*np.cos(2*np.pi*self.frequency*self.nodes[0][TIME])) * np.cos(2*np.pi*self.carrierFrequency*self.nodes[0][TIME]) # genero señal AM
        else:  # asumo que es 3/2 seno
            i = 0
            j = 0
            while i < len(self.nodes[0][TIME]):
                if self.nodes[0][TIME][i] < (j + 1) * self.signalPeriod:
                    self.nodes[0][VALUE][i] = self.amplitude * np.sin(2 * np.pi * self.frequency * (3/2) * (self.nodes[0][TIME][i] - j * self.signalPeriod))
                    i += 1
                else:
                    j += 1

        return

    # emulateAAFilter()
    # emula el filtro anti-aliasing del circuito sobre un determinado arreglo
    def emulateAAFilter(self):
        self.nodes[1] = deepcopy(self.nodes[0])

        antiAlias1 = sps.lti(ZEROS1, POLES1, 1)  # genero objeto funcion transferencia del filtro
        antiAlias2 = sps.lti(ZEROS2, POLES2, 1)
        antiAlias3 = sps.lti(ZEROS3, POLES3, 1)
        antiAlias4 = sps.lti(ZEROS4, POLES4, GAIN)

        x, y, _ = antiAlias1.output(self.nodes[1][VALUE], self.nodes[1][TIME])
        x, y, _ = antiAlias2.output(y, x)
        x, y, _ = antiAlias3.output(y, x)
        x, y, _ = antiAlias4.output(y, x)

        self.nodes[1][TIME] = x
        self.nodes[1][VALUE] = y
        return

    # emulateRecoveryFilter()
    # emula el filtro de recuperación del circuito sobre un determinado arreglo
    def emulateRecoveryFilter(self):
        self.nodes[4] = deepcopy(self.nodes[3])
        
        recovery1 = sps.lti(ZEROS1, POLES1, 1)    # genero objeto funcion transferencia del filtro
        recovery2 = sps.lti(ZEROS2, POLES2, 1)
        recovery3 = sps.lti(ZEROS3, POLES3, 1)
        recovery4 = sps.lti(ZEROS4, POLES4, GAIN)
        
        x, y, _ = recovery1.output(self.nodes[4][VALUE], self.nodes[4][TIME])
        x, y, _ = recovery2.output(y,x)
        x, y, _ = recovery3.output(y,x)
        x, y, _ = recovery4.output(y,x)
        
        self.nodes[4][TIME] = x
        self.nodes[4][VALUE] = y
        return


    # emulateSampleNHold()
    # emula el sample & hold del circuito
    def emulateSampleNHold(self):
        self.nodes[2] = deepcopy(self.nodes[1])
        i = 1
        j = 1                                            # set en 1 dado que el primer valor del arreglo se considera muestreado
        while i < len(self.nodes[2][TIME]):                        # para cada elemento del arreglo
            if (self.nodes[2][TIME][i] - self.nodes[2][TIME][0]) < j*self.samplePeriod: # arr[TIME][0] representa el tiempo inicial
                self.nodes[2][VALUE][i] = deepcopy(self.nodes[2][VALUE][i-1])          # asigno valor anterior al actual
            else:
                j += 1                                   # incremento contador de períodos
            i += 1
        return

    # emulateAnalogSwitch()
    # emula la llave analógica del circuito
    def emulateAnalogSwitch(self):
        self.nodes[3] = deepcopy(self.nodes[2])
        i = 0
        j = 0
        while i < len(self.nodes[3][TIME]):
            if (self.nodes[3][TIME][i] - self.nodes[3][TIME][0]) < (j+1)*self.samplePeriod:
                if (self.nodes[3][TIME][i] - self.nodes[3][TIME][0]) > (j*self.samplePeriod + self.tau):
                    self.nodes[3][VALUE][i] = 0   # fuera del pulso
                i += 1
            else:
                j += 1                         # si esta fuera de rango, incremento contador de periodos
        return

    # fourierTransform()
    # devuelve la transformada rápida de Fourier (FFT) de una señal periódica
    # CONSIDERACIONES:
    #   - cada nodo debe contener una cantidad entera de períodos de la señal a transformar
    #   - se establece un mínimo de 5 períodos de la señal, para que el gráfico final sea representativo del espectro
    def fourierTransform(self, node_num):
        w = sps.windows.blackman(POINTS)
        fy = np.fft.fft(self.nodes[node_num][VALUE] * w) / POINTS  # transformada de fourier
        fx = np.fft.fftfreq(self.nodes[node_num][TIME].size, (max(self.nodes[node_num][TIME]) - min(self.nodes[node_num][TIME])) / POINTS) # frecuencias
        return fx, fy

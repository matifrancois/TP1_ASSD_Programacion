import scipy.signal as sps
import numpy as np

# CANTIDAD DE PUNTOS POR NODO
POINTS = 1000

# COEFICENTES DE LOS FILTROS DEL CIRCUITO
AAS_NUM = []
AAS_DEN = []
REC_NUM = []
REC_DEN = []

# CONSTANTES FUNCIONALES DEL PROGRAMA
TIME = 0
VALUE = 1


class Backend():
    """ Creamos nuestra clase MatplotlibWidget, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """
    def __init__(self):
        super(Backend, self).__init__()        # Llamamos al constructor de los padres
        # self.setupUi(self)# Necesitamos usar esto para hacer el build de los componentes
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
        self.nodes = [[np.zeros(POINTS), np.zeros(POINTS)],
                     [np.zeros(POINTS), np.zeros(POINTS)],
                     [np.zeros(POINTS), np.zeros(POINTS)],
                     [np.zeros(POINTS), np.zeros(POINTS)],
                     [np.zeros(POINTS), np.zeros(POINTS)]]

    def check_input(self, diccionario):
        """
        comprueba que los valores del diccionario tengan sentido sino devuelve un flag y el string con el comentario
        indicando por que no tuvo sentido
        :param diccionario:
        :return: flag (0 all bien o -1 all mal), string
        """
        if diccionario["amplitud"].isdigit():
            return 0, ""
        else:
            return -1, "amplitud no es digito"

    # getNode()
    # devuelve la información en tiempo del nodo indicado
    def getNode(self, node_num):
        return self.nodes[node_num]

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
            self.tau = float(fields[6].split(':')[1])

        else:
            self.carrierAmplitude = float(fields[1].split(':')[1])
            self.carrierFrequency = float(fields[2].split(':')[1])
            self.amplitude = float(fields[3].split(':')[1])     # moduladora
            self.frequency = float(fields[4].split(':')[1])     # moduladora
            self.modulationFactor = float(fields[5].split(':')[1])
            self.samplePeriod = float(fields[6].split(':')[1])
            self.period_qty = float(fields[7].split(':')[1])
            self.tau = float(fields[8].split(':')[1])

        self.signalPeriod = 1/self.frequency

        return



    # emulateCircuit()
    # emula cada nodo del circuito para una determinada configuración.
    def emulateCircuit(self, circuitTopology):

        if circuitTopology[0] == '1':
            self.emulateAAFilter()
        else:
            self.nodes[1] = self.nodes[0]

        if circuitTopology[1] == '1':
            self.emulateSampleNHold()
        else:
            self.nodes[2] = self.nodes[1]

        if circuitTopology[2] == '1':
            self.emulateAnalogSwitch()
        else:
            self.nodes[3] = self.nodes[2]

        if circuitTopology[3] == '1':
            self.emulateRecoveryFilter()
        else:
            self.nodes[4] = self.nodes[3]

        return

    # generateinput()
    # genera el primer nodo del circuito, teniendo en cuenta los parametros de la señal que recibe del objeto
    def generateInput(self):
        self.nodes[0][TIME] = np.arange(0, self.period_qty*self.signalPeriod, (self.period_qty*self.signalPeriod) / POINTS)  # creo eje temporal

        if self.signalType == "Senoidal":
            self.nodes[0][VALUE] = self.amplitude * np.sin(2 * np.pi * self.frequency * self.nodes[0][TIME])  # genero señal senoidal
        elif self.signalType == "Cuadratica":
            raise NameError("Completar cuadratica")
        elif type == "AM":
            self.nodes[0][VALUE] = self.carrierAmplitude * (1+self.modulationFactor*self.amplitude*np.cos(2*np.pi*self.frequency*self.nodes[0][VALUE])) * np.cos(2*np.pi*self.carrierFrequency*self.nodes[0][VALUE]) # genero señal AM
        else:  # asumo que es 3/2 seno
            i = 0
            j = 0
            while i < len(self.nodes[0][TIME]):
                if self.nodes[0][TIME][i] < (j + 1) * (3 / 2) * self.period:
                    self.nodes[0][VALUE][i] = self.amplitude * np.sin(2 * np.pi * self.frequency * (self.nodes[0][TIME][i] - j * (3 / 2) * self.period))
                    i += 1
                else:
                    j += 1

        return

    # emulateAAFilter()
    # emula el filtro anti-aliasing del circuito sobre un determinado arreglo
    def emulateAAFilter(self):
        antiAlias = sps.lti(AAS_NUM,AAS_DEN)    # genero objeto funcion transferencia del filtro
        self.nodes[1][VALUE] = antiAlias.output(self.nodes[0][VALUE],self.nodes[0][TIME])
        return

    # emulateRecoveryFilter()
    # emula el filtro de recuperación del circuito sobre un determinado arreglo
    def emulateRecoveryFilter(self):
        recovery = sps.lti(REC_NUM, REC_DEN)    # genero objeto funcion transferencia del filtro
        self.nodes[4][VALUE] = recovery.output(self.nodes[3][VALUE], self.nodes[3][TIME])
        return


    # emulateSampleNHold()
    # emula el sample & hold del circuito
    def emulateSampleNHold(self):
        arr = self.nodes[1]
        i = 1
        j = 1                                            # set en 1 dado que el primer valor del arreglo se considera muestreado
        while i < len(arr[TIME]):                        # para cada elemento del arreglo
            if (arr[TIME][i] - arr[TIME][0]) < j*self.samplePeriod: # arr[TIME][0] representa el tiempo inicial
                arr[VALUE][i] = arr[VALUE][i-1]          # asigno valor anterior al actual
            else:
                j += 1                                   # incremento contador de períodos
            i += 1
        self.nodes[2] = arr
        return

    # emulateAnalogSwitch()
    # emula la llave analógica del circuito
    def emulateAnalogSwitch(self):
        arr = self.nodes[2]
        i = 0
        j = 0
        while i < len(arr[TIME]):
            if (arr[TIME][i] - arr[TIME][0]) < (j+1)*self.samplePeriod:
                if (arr[TIME][i] - arr[TIME][0]) > (j*self.samplePeriod + self.tau):
                    arr[VALUE][i] = 0   # fuera del pulso
                i += 1
            else:
                j += 1                         # si esta fuera de rango, incremento contador de periodos
        self.nodes[3] = arr
        return

    # fourierTransform()
    # devuelve la transformada rápida de Fourier (FFT) de una señal periódica
    # CONSIDERACIONES:
    #   - cada nodo debe contener una cantidad entera de períodos de la señal a transformar
    #   - se establece un mínimo de 5 períodos de la señal, para que el gráfico final sea representativo del espectro
    def fourierTransform(self, node_num):
        fy = np.fft.fft(self.nodes[node_num]) / POINTS # transformada de fourier normalizada
        fx = np.fft.fftfreq(self.nodes[node_num][TIME].size, (max(self.nodes[node_num][TIME]) - min(self.nodes[node_num][TIME])) / POINTS) # frecuencias
        return [fx, fy]

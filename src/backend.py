from numpy import *

class Backend:
    """ Creamos nuestra clase MatplotlibWidget, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """
    def __init__(self):
        super(Backend, self).__init__()        # Llamamos al constructor de los padres
        # self.setupUi(self)# Necesitamos usar esto para hacer el build de los componentes
        self.senial = ""
        self.amplitud = 0.0
        self.frecuencia = 0.0
        self.llaves = 0
        self.T = 0.0
        self.tau = 0.0
        self.x_s = []
        self.y_s = []
        self.x_f = []
        self.y_f = []

    """"
    def set_input(self, diccionario):
        self.senial = diccionario['senial_elegida']
        if diccionario['amplitud'].isdigit():
            self.amplitud = float(diccionario['amplitud'])
        else:
            self.amplitud = 0
        if diccionario['frecuencia'].isdigit():
            self.frecuencia = float(diccionario['frecuencia'])
        else:
            self.frecuencia = 0
        self.llaves = diccionario['llaves']
        if diccionario['tau'].isdigit():
            self.tau = float(diccionario['tau'])
        else:
            self.tau = 0
        if diccionario['T'].isdigit():
            self.T = float(diccionario['T'])
        else:
            self.T = 0
    """


    def devuelvo(self, nodo, senial_a_graficar, x):
        """
        aca es donde tendria que trabajar joaco con el backend
        """

        self.x_s = linspace(0, 4 * pi, num=1000)
        self.y_s = self.amplitud*sin(self.frecuencia * self.x_s)
        self.x_f = linspace(0, 1 * pi, num=1000)
        self.y_f = sin(6 * self.x_f)
        return self.x_s, self.y_s, self.x_f, self.y_f

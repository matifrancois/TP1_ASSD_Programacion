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
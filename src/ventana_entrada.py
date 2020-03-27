class   Ventana_Entrada:
    """ Creamos nuestra clase Ventana_Entrada, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """

    def __init__(self):
        super(Ventana_Entrada, self).__init__()        # Llamamos al constructor de los padres
        self.setupUi(self)
        self.comboBox_senial.currentIndexChanged.connect(self.cambie_de_eleccion)
        self.pushButton_ok.clicked.connect(self.getItem)
        self.frecuencia=0

    def cambie_de_eleccion(self):
        self.senial_elegida = self.comboBox_senial.currentText()
        if self.senial_elegida == "Cuadratica":
            self.lineEdit_frecuencia.setDisabled(True)
        else:
            self.lineEdit_frecuencia.setDisabled(False)


    def getItem(self):
        self.senial_elegida = self.comboBox_senial.currentText()
        self.amplitud = self.lineEdit_amplitud.text()
        self.frecuencia = self.lineEdit_frecuencia.text()
        print(self.senial_elegida)
        print(self.amplitud)
        print(self.frecuencia)
        self.close()
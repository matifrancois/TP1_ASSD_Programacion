from src.ui.ventanaEntrada import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QDialog, QComboBox, QApplication
import sys

class Ventana_Entrada(QDialog, Ui_Dialog):
    """ Creamos nuestra clase Ventana_Entrada, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """

    def __init__(self):
        super(QDialog, self).__init__()        # Llamamos al constructor de los padres
        self.setupUi(self)
        # solo utilizar la siguiente expresion si un parametro debe quedar inhabilitado al igual que cambia_de_elecccion
        # self.comboBox_senial.currentIndexChanged.connect(self.cambie_de_eleccion)
        self.buttonBox.clicked.connect(self.getItem)
        self.frecuencia = 0

    def getItem(self):
        self.senial_elegida = self.comboBox_senial.currentText()
        self.amplitud = self.lineEdit_amplitud.text()
        self.frecuencia = self.lineEdit_frecuencia.text()
        #self.mandarinfo()
        #app = QApplication(sys.argv)
        #if app.exec() == QDialog.Accepted:         #TODO aqui ver como pasar los datos al backend como dijo lucas
        #    print("hola")
        #else:
        #    print("chau")

    # def mandarinfo(self):
        """
        Esta funcion se encarga de enviar la info obtenida al backend
        :return:
        """


    """def cambie_de_eleccion(self):
            """"""
            funcion que se encarga de inhabilitar la entrada de datos en las situaciones requeridas
            :return: 
            """"""
            self.senial_elegida = self.comboBox_senial.currentText()
            if self.senial_elegida == "Cuadratica":
                self.lineEdit_frecuencia.setDisabled(True)
            else:
                self.lineEdit_frecuencia.setDisabled(False)
        """

from datetime import datetime
import csv

# Librerias para impresion
import win32print
import win32api
from glob import glob

class GestorConsultarEncuesta:
    def __init__(self, 
    pantallaConsultarEncuesta = None, 
    llamadas = [],
    fechaInicioPeriodo = datetime.now(), 
    fechaFinPeriodo = datetime.now(),
    llamadasDePeriodo = []
    ):
        self.pantalla = pantallaConsultarEncuesta
        self.llamadas = llamadas
        self.fechaInicioPeriodo = fechaInicioPeriodo
        self.fechaFinPeriodo = fechaFinPeriodo
        self.llamadasDePeriodo = llamadasDePeriodo

    def nuevaConsultaEncuesta(self):
        self.pantalla.pedirPeriodo()

    def tomarPeriodo(self, fechaInicio, fechaFin):
        self.fechaInicioPeriodo = fechaInicio
        self.fechaFinPeriodo = fechaFin
        self.buscarLlamadas()

    def buscarLlamadas(self):
        '''
        for llamada in self.llamadas:
            if llamada.esDePeriodo(self.fechaInicioPeriodo, self.fechaFinPeriodo):
                self.llamadasDePeriodo.append(llamada)
        '''
        # HARDCODED
        # Cambiar llamadas por llamadas de periodo cuando este implementado
        self.pantalla.pedirSeleccionLlamada(self.llamadas)

    def tomarSeleccionLlamada(self, indexLlamada):
        # HARDCODED
        preguntas = [['Pregunta 1', 'Respuesta 1'], ['Pregunta 2', 'Respuesta 2'], ['Pregunta 3', 'Respuesta 3']]
        self.pantalla.pedirSeleccionSalida('(Nombre cliente)', '(Estado actual)', '(duracion)', '(encuesta realizada)', preguntas)

    def buscarDatosRtas(self):
        pass

    def tomarSeleccionCSV(self):
        self.generarCsv()

    def obtenerImpresoras(self):
        # win32print.PRINTER_ENUM_LOCAL para enumerar impresoras locales
        # El segundo parametro es el servidor de impresoras. Como queremos las locales, pasamos None
        # El tercer parametro es el nivel de detalle. 1 es el minimo
        impresoras = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        # El nombre de la impresora es el segundo elemento de la tupla
        return [impresora[2] for impresora in impresoras]

    def tomarSeleccionImpresion(self):
        self.pantalla.pedirSeleccionImpresora(self.obtenerImpresoras())

    def imprimir(self, nombreImpresora):
        # Create a temporal txt file to print
        fileDir = 'temp.txt'
        # HARDCODED
        f = open('temp.txt', 'w+t')
        f.write('test 2')
        f.close()

        # Print the txt file
        win32print.SetDefaultPrinter(nombreImpresora)
        for f in glob(fileDir, recursive = True):
            win32api.ShellExecute(0, "print", fileDir, None,  ".",  0)

        self.finCU()

    def generarCsv(self):
        # HARDCODED
        row_list = [["SNo", "Name", "Subject"],
              [1, "Ash Ketchum", "English"],
              [2, "Gary Oak", "Mathematics"],
              [3, "Brock Lesner", "Physics"]]

        with open('temp.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)

        self.finCU()

    def finCU(self):
        pass
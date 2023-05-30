from datetime import datetime
import csv

# Librerias para impresion
import win32print
import win32api
from glob import glob

class GestorConsultarEncuesta:
    def __init__(self, 
    pantalla = None, 
    llamadas = [],
    encuestas = [],
    fechaInicioPeriodo = datetime.now(), 
    fechaFinPeriodo = datetime.now(),
    llamadasDePeriodo = [],
    nombreClienteDeLlamada = '',
    estadoLlamada = None,
    duracionLlamada = 0,
    preguntasYRtasSeleccionadas = [],
    descripcionEncuesta = ''
    ):
        self.pantalla = pantalla
        self.llamadas = llamadas
        self.encuestas = encuestas

        self.fechaInicioPeriodo = fechaInicioPeriodo
        self.fechaFinPeriodo = fechaFinPeriodo
        self.llamadasDePeriodo = llamadasDePeriodo
        self.nombreClienteDeLlamada = nombreClienteDeLlamada
        self.estadoLlamada = estadoLlamada
        self.duracionLlamada = duracionLlamada
        self.preguntasYRtasSeleccionadas = preguntasYRtasSeleccionadas
        self.descripcionEncuesta = descripcionEncuesta

    def setPantalla(self, pantallaConsultarEncuesta):
        self.pantalla = pantallaConsultarEncuesta

    def nuevaConsultaEncuesta(self):
        self.pantalla.pedirPeriodo()

    def tomarPeriodo(self, fechaInicio, fechaFin):
        self.fechaInicioPeriodo = fechaInicio
        self.fechaFinPeriodo = fechaFin
        self.buscarLlamadas()

    def buscarLlamadas(self):
        self.llamadasDePeriodo = []
        for llamada in self.llamadas:
            if llamada.esDePeriodo(self.fechaInicioPeriodo, self.fechaFinPeriodo):
                self.llamadasDePeriodo.append(llamada)

        self.llamadasDePeriodo.sort(key = lambda x: x.obtenerFechaHoraInicio())
        fechasLlamadas = []
        for llamada in self.llamadasDePeriodo:
            fechasLlamadas.append(datetime.strftime(llamada.obtenerFechaHoraInicio(), '%d/%m/%Y %H:%M:%S'))

        self.pantalla.pedirSeleccionLlamada(fechasLlamadas)

    def buscarDatosLlamada(self, indexLlamada):
        self.nombreClienteDeLlamada = self.llamadasDePeriodo[indexLlamada].getNombreClienteDeLlamada()
        self.estadoLlamada = self.llamadasDePeriodo[indexLlamada].getEstadoActual()
        self.duracionLlamada = self.llamadasDePeriodo[indexLlamada].getDuracion()

    def tomarSeleccionLlamada(self, indexLlamada):
        self.buscarDatosLlamada(indexLlamada)
        # HARDCODED
        respuestas = self.llamadasDePeriodo[indexLlamada].getRespuestas()
        self.preguntasYRtasSeleccionadas = []

        preguntas = []
        self.descripcionEncuesta = ''
        for encuesta in self.encuestas:
            for pregunta in encuesta.getPreguntas():
                for respuestasEncuesta in pregunta.getRtas():
                    for respuestaSeleccionada in respuestas:
                        if respuestasEncuesta == respuestaSeleccionada.getRespuestaSeleccionada():
                            preguntas.append(pregunta.getDescripcion())
                            self.descripcionEncuesta = encuesta.getDescripcionEncuesta()
                            
        for i in range(len(respuestas)):
            self.preguntasYRtasSeleccionadas.append([preguntas[i], respuestas[i].getDescripcionRta()])

        self.pantalla.pedirSeleccionSalida(
            self.nombreClienteDeLlamada, 
            self.estadoLlamada, 
            self.duracionLlamada, 
            self.descripcionEncuesta, 
            self.preguntasYRtasSeleccionadas)

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

        f.write('{}, {}, {}\n'.format(self.nombreClienteDeLlamada, self.estadoLlamada, self.duracionLlamada))
        for i in range (len(self.preguntasYRtasSeleccionadas)):
            f.write('{}, {}\n'.format(self.preguntasYRtasSeleccionadas[i][0], self.preguntasYRtasSeleccionadas[i][1]))

        f.close()

        # Print the txt file
        win32print.SetDefaultPrinter(nombreImpresora)
        for f in glob(fileDir, recursive = True):
            win32api.ShellExecute(0, "print", fileDir, None,  ".",  0)

        self.finCU()

    def generarCsv(self):
        # HARDCODED
        row_list = [[self.nombreClienteDeLlamada, self.estadoLlamada, self.duracionLlamada]]
        for preguntaYRta in self.preguntasYRtasSeleccionadas:
            row_list.append(preguntaYRta)

        with open('temp.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)

        self.finCU()

    def finCU(self):
        pass

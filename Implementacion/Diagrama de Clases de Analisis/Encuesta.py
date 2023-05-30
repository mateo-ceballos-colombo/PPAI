import Pregunta
import random
import random as rnd
from datetime import datetime
import FechaYHora

class Encuesta:
    def __init__(self, descripcion='', fechaFinVigencia='', preguntas=None):
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia
        self.preguntas = preguntas

    def armarEncuesta(self):
        pass

    def esEncuestaDeCliente(self):
        pass

    def esVigente(self):
        if self.fechaFinVigencia > dt.datetime.now():
            return True
        return False

    def getDescripcionEncuesta(self):
        return self.descripcion
    
    def __str__(self):
        r = ''
        r += '{:<50}\n'.format('Descripción de la encuesta: ' + self.descripcion)
        r += '{:<30}\n'.format('Fecha de fin de vigencia: ' + datetime.strftime(self.fechaFinVigencia, "%d/%m/%Y %H:%M:%S"))
        r += 'Preguntas: \n'
        for pregunta in self.preguntas:
            r += '- {:<30}'.format(str(pregunta))
            r += '\n'
        return r

class adhoc:
    descrip = ['Encuesta de satisfaccion', 'Encuesta de calidad', 'Encuesta de servicio', 
    'Encuesta de producto', 'Encuesta de atencion al cliente', 'Encuesta de atencion al publico']

    def generarEncuestasAleatorias(self, cantidadEncuestas):

        encuestas = cantidadEncuestas * [None]

        for i in range(cantidadEncuestas):
            descripcion = random.choice(self.descrip)
            randomDate = FechaYHora.obtenerFechaHoraRandom(endDate=datetime(2030, 12, 31))
            # Se debe generar 2 o 3 preguntas aleatorias para cada encuesta
            preguntasRandom = Pregunta.adhoc().generarPreguntasAleatorias(rnd.randint(2, 3))
            encuestas[i] = Encuesta(descripcion, randomDate, preguntasRandom)
        
        return encuestas

    def mostrar(self, vector):
        print('----Encuestas----')
        for i in range(len(vector)):
            print(vector[i])
            print('---------------------------------')


def main():
    n = int(input('Ingrese la cantidad de encuestas a generar: '))

    encuestasAdhoc = adhoc()
    encuestas = encuestasAdhoc.generarEncuestasAleatorias(n)
    encuestasAdhoc.mostrar(encuestas)
    

if __name__ == '__main__':
    main()
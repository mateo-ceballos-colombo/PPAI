import Pregunta
import random
import random as rnd
import datetime as dt
import FechaYHora

class Encuesta:
    def __init__(self, descripcion='', fechaFinVigencia='', preg=None):
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia
        self.preguntas = preg

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

class adhoc:
    descrip = ['Encuesta de satisfaccion', 'Encuesta de calidad', 'Encuesta de servicio', 
    'Encuesta de producto', 'Encuesta de atencion al cliente', 'Encuesta de atencion al publico']

    def generarEncuestaAleatoria(self, cantidadEncuestas, encuestas):

        for i in range(cantidadEncuestas):
            descripcion = random.choice(self.descrip)
            encuestas[i] = Encuesta(descripcion)
            random_date = FechaYHora.obtenerFechaHoraRandom()
            encuestas[i].fechaFinVigencia = random_date

            # Se debe generar 2 o 3 preguntas aleatorias para cada encuesta
            encuestas[i].m_Pregunta = Pregunta.adhoc.generarPreguntasAleatorias(rnd.randint(2, 3))

        print('Encuestas generadas con exito')

    def mostrar(vector):
        print('----Encuestas----')
        for i in range(len(vector)):
            print('Encuesta ', i + 1)
            print('Descripcion: ', vector[i].descripcion)
            print('Fecha de fin de vigencia: ', vector[i].fechaFinVigencia)
            print('Preguntas: ')
            for j in range(len(vector[i].m_Pregunta)):
                print(vector[i].m_Pregunta[j].pregunta)
            print('---------------------------------')


def main():
    n = int(input('Ingrese la cantidad de encuestas a generar: '))

    encuestas = n * [None]
    generarEncuestaAleatoria(n, encuestas)
    mostrar(encuestas)
    

if __name__ == '__main__':
    main()
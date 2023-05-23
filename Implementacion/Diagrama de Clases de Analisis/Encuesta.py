
#import Pregunta
import random as rnd
import datetime as dt
import sys

class Encuesta:
    def __init__(self, des='', fec='', preg=Pregunta()):
        self.descripcion = des
        self.fechaFinVigencia = fec
        self.m_Pregunta = preg

    def armarEncuesta():
        pass

    def esEncuestaDeCliente():
        pass

    def esVigente():
        pass

    def getDescripcionEncuesta():
        pass


nomEncuestas = ['Encuesta de satisfaccion', 'Encuesta de calidad', 'Encuesta de servicio', 
    'Encuesta de producto', 'Encuesta de atencion al cliente', 'Encuesta de atencion al publico']

def generarEncuestaAleatoria(cantidadEncuestas, encuestas):

    if cantidadEncuestas > len(nomEncuestas):
        print('La cantidad de encuestas a generar es mayor a la cantidad de encuestas disponibles')
        sys.exit()

    for i in range(cantidadEncuestas):
        encuestas[i] = Encuesta()
        encuestas[i].descripcion = nomEncuestas[i]
        current_year = dt.datetime.now().year
        random_date = dt.date(rnd.randint(current_year, (current_year + 10)), rnd.randint(1, 12), rnd.randint(1, 28))
        encuestas[i].fechaFinVigencia = random_date
        # ~Sobre la siguiente linea: se debe generar 2 o 3 preguntas aleatorias para cada encuesta
        encuestas[i].m_Pregunta = Pregunta.generarPreguntasAleatorias(rnd.randint(2, 3))
           
    print('Encuestas generadas con exito')

def test():
    n = int(input('Ingrese la cantidad de encuestas a generar: '))
    encuestas = n * [None]
    generarEncuestaAleatoria(n, encuestas)
    for i in range(n):
        print('Encuesta: ', i + 1)
        print('Descripcion: ', encuestas[i].descripcion)
        print('Fecha de fin de vigencia: ', encuestas[i].fechaFinVigencia)

test()




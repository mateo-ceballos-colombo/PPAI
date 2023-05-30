
import Pregunta
import random as rnd
import datetime as dt

class Encuesta:
    def __init__(self, des='', fec='', preg=None):
        self.descripcion = des
        self.fechaFinVigencia = fec
        self.m_Pregunta = preg

    def armarEncuesta(self):
        #encuestas = [None]
        #generarEncuestaAleatoria(1, encuestas)
        #return encuestas
        pass

    def esEncuestaDeCliente(self):
        pass

    def esVigente(self):
        if self.fechaFinVigencia > dt.datetime.now():
            return True
        else:
            return False

    def getDescripcionEncuesta(self):
        return self.descripcion


nomEncuestas = ['Encuesta de satisfaccion', 'Encuesta de calidad', 'Encuesta de servicio', 
    'Encuesta de producto', 'Encuesta de atencion al cliente', 'Encuesta de atencion al publico']

def generarEncuestaAleatoria(cantidadEncuestas, encuestas):

    for i in range(cantidadEncuestas):
        encuestas[i] = Encuesta()
        encuestas[i].descripcion = nomEncuestas[i]
        current_year = dt.datetime.now().year
        random_date = dt.date(rnd.randint(current_year, (current_year + 10)), rnd.randint(1, 12), rnd.randint(1, 28))
        encuestas[i].fechaFinVigencia = random_date
        # ~Sobre la siguiente linea: se debe generar 2 o 3 preguntas aleatorias para cada encuesta
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
    while n > len(nomEncuestas):
        n = int(input('La cantidad de encuestas a generar es mayor a la cantidad de encuestas disponibles. Ingrese una cantidad menor: '))
        
    encuestas = n * [None]
    generarEncuestaAleatoria(n, encuestas)
    mostrar(encuestas)
    

if __name__ == '__main__':
    main()
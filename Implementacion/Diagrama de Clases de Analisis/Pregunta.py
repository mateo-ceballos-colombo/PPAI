import random
import RespuestaPosible

class Pregunta:
    def __init__(self, preg='', resp=None):
        self.pregunta = preg
        self.m_respuestaPosible = resp

    def getDescripcion(self):
        pass

    def listarRespuestasPosibles(self):
        pass

preguntasRandom = {
    1: ['¿Le gustó la atención?', []],
    2: ['¿Del 1 al 10 en cuánto nos calificaría?', []],
    3: ['¿Nos recomendaría a otras personas?', []]
}

def generarPreguntasAleatorias(cantidadPreguntas, preguntas):
    for i in range(cantidadPreguntas):
        preguntas[i] = Pregunta()
        preguntas[i].pregunta = preguntasRandom[i+1][0]
        if preguntas[i].pregunta == preguntasRandom[2][0]:
            preguntas[i].m_respuestaPosible = RespuestaPosible.adhoc.generarRespuestas(1, 1)  # Cambié 'vector' por 2
        else: 
            preguntas[i].m_respuestaPosible = RespuestaPosible.adhoc.generarRespuestas(1, 2)
        
    print('Preguntas generadas con éxito')

def test():
    n = int(input('Ingrese la cantidad de preguntas a generar (3 o menos): '))
    while 0 < n > 3:
        n = int(input('Por favor ingrese 3 o menos:'))
    preguntas = n * [None]
    generarPreguntasAleatorias(n, preguntas)
    for i in range(n):
        print('Pregunta:', i + 1)
        print('Descripción:', preguntas[i].pregunta)
        print('Respuestas posibles:')
        for respuesta in preguntas[i].m_respuestaPosible:
            print(respuesta.descripcion, '-', respuesta.valor)

def main():
    pass

if __name__ == '__main__':
    test()


import RespuestaPosible
import random



class Pregunta:
    def __init__(self, preg='', resp=None): #, resp=None y antes estaba self.m_respuestaPosible = resp
        self.pregunta = preg
        self.m_respuestaPosible = resp

    def getDescripcion():
        pass

    def listarRespuestasPosibles():
        pass


preguntasRandom = {
    1: ['¿Le gustó la atención?', []],
    2: ['¿Del 1 al 10 en cuánto nos calificaría?', []],
    3: ['¿Nos recomendaría a otras personas?', []]
}
#    1: ['¿Le gustó la atención?', [self.m_respuestaPosible[0], self.m_respuestaPosible[1]]],


def generarPreguntasAleatorias(cantidadPreguntas, preguntas):
    vector = cantidadPreguntas * [None]
    for i in range(cantidadPreguntas):
        preguntas[i] = Pregunta()
        preguntas[i].pregunta = preguntasRandom[i+1][0]
        preguntas[i].m_respuestaPosible = RespuestaPosible.adhoc.generarRespuestas(vector, cantidadPreguntas)
        #respuestas = RespuestaPosible.adhoc.generarRespuestas(vector, cantidadPreguntas)
        #preguntas[i].m_respuestaPosible = respuestas[i]
    
    print('Preguntas generadas con exito')

def test():
    n = int(input('Ingrese la cantidad de preguntas a generar: '))
    preguntas = n * [None]
    generarPreguntasAleatorias(n, preguntas)
    for i in range(n):
        print('Pregunta: ', i + 1)
        print('Descripcion: ', preguntas[i].pregunta)
        print('Respuestas posibles: ', preguntas[i].m_respuestaPosible)

def main():
    pass

if __name__ == '__main__':
    test()



"""

class Pregunta:
    def __init__(self, preg='', resp=RespuestaPosible.RespuestaPosible()):
        self.pregunta = preg
        self.m_respuestaPosible = resp 
        
    def getDescripcion():
"""


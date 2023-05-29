import random
import RespuestaPosible

class Pregunta:
    def __init__(self, preg='', resp=None):
        self.pregunta = preg
        self.respuestas = resp

    def getDescripcion(self):
        return self.pregunta

    def listarRespuestasPosibles(self):
        return self.respuestas[0].getDescripcionRta()

class adhoc:
    def generarPreguntasAleatorias(cantidadPreguntas):
        preguntasRandom = [
            ['¿Le gustó la atención?', []],
            ['¿Del 1 al 10 en cuánto nos calificaría?', []],
            ['¿Nos recomendaría a otras personas?', []]
        ]

        rtaPosibleadhoc = RespuestaPosible.adhoc()

        preguntas = cantidadPreguntas * [None]

        for i in range(cantidadPreguntas):
            preguntaRandom = preguntasRandom[i][0]
            
            if preguntas[i].pregunta == preguntasRandom[1][0]:
                respuestaPosible = rtaPosibleadhoc.generarRespuestas(1, 0)
            else: 
                respuestaPosible = rtaPosibleadhoc.generarRespuestas(1, 1)

            preguntas[i] = Pregunta(preguntaRandom, respuestaPosible)
        
        return preguntas


def test():
    n = int(input('Ingrese la cantidad de preguntas a generar (3 o menos): '))
    while n < 0 or n > 3:
        n = int(input('Ingrese la cantidad de preguntas a generar (3 o menos): '))
    
    preguntas = adhoc().generarPreguntasAleatorias(n)
    for i in range(n):
        print('Pregunta:', i + 1)
        print('Descripción:', preguntas[i].pregunta)
        print('Respuestas posibles:')
        for respuesta in preguntas[i].m_respuestaPosible:
           print(respuesta.getDescripcionRta())
        #print(preguntas.m_respuestaPosible.getDescripcionRta(preguntas[i].m_respuestaPosible[0]))

if __name__ == '__main__':
    test()

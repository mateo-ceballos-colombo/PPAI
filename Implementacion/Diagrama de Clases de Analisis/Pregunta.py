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
        preguntasRandomBool = [
            ['¿Le gustó la atención?'],
            ['¿Nos recomendaría a otras personas?'],
            ['¿Recibiste una respuesta o solución a tu consulta o problema?'],
            ['¿Experimentaste alguna dificultad técnica o de comunicación durante la interacción?'],
            ['¿El personal de atención al cliente demostró conocimiento y competencia en su respuesta?']
        ]
        preguntasRandomNros = [
            ['Del 1 al 10, ¿en cuánto nos calificaría?'],
            ['Del 1 al 10, ¿qué tan fácil fue contactar a nuestro servicio de atención al cliente?'],
            ['Del 1 al 10, ¿qué tan bien resolvimos tu consulta o problema?'],
            ['Del 1 al 10, ¿qué tan rápido fue el tiempo de respuesta de nuestro equipo de atención al cliente?']
        ]

        rtaPosibleAdhoc = RespuestaPosible.adhoc()

        preguntas = cantidadPreguntas * [None]

        for i in range(cantidadPreguntas):
            preguntaRandom = random.sample(preguntasRandomBool + preguntasRandomNros, 1)

            for j in range(preguntasRandomBool):
                if preguntaRandom == j:
                    respuestaPosible = rtaPosibleadhoc.generarRespuestas(1, 1)
                else: 
                    respuestaPosible = rtaPosibleadhoc.generarRespuestas(1, 0)

            preguntas[i] = Pregunta(preguntaRandom, respuestaPosible)
        
        return preguntas


def test():
    n = int(input('Ingrese la cantidad de preguntas a generar (3 o menos): '))
    while n < 0 or n > 3:
        n = int(input('Ingrese la cantidad de preguntas a generar (3 o menos): '))
    
    preguntas = adhoc.generarPreguntasAleatorias(n)
    for i in range(n):
        print('Pregunta:', i + 1)
        print('Descripción:', preguntas[i].pregunta)
        print('Respuestas posibles:')
        for respuesta in preguntas[i].respuestaPosible:
           print(respuesta.getDescripcionRta())
        #print(preguntas.m_respuestaPosible.getDescripcionRta(preguntas[i].m_respuestaPosible[0]))

if __name__ == '__main__':
    test()
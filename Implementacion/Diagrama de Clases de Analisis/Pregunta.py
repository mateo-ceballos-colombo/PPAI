import random
import RespuestaPosible

class Pregunta:
    def __init__(self, preg='', resp=None):
        self.pregunta = preg
        self.respuestas = resp

    def getDescripcion(self):
        return self.pregunta

    def listarRespuestasPosibles(self):
        respuestasPosibles = []
        for i in range(len(self.respuestas)):
            respuestasPosibles.append(self.respuestas[i].getValorRta())
        return respuestasPosibles

class adhoc:
    def generarPreguntasAleatorias(cantidadPreguntas):
        preguntasRandomBool = [
            '¿Le gustó la atención?',
            '¿Nos recomendaría a otras personas?',
            '¿Recibiste una respuesta o solución a tu consulta o problema?',
            '¿Experimentaste alguna dificultad técnica o de comunicación durante la interacción?',
            '¿El personal de atención al cliente demostró conocimiento y competencia en su respuesta?'
        ]
        preguntasRandomNros = [
            'Del 1 al 10, ¿en cuánto nos calificaría?',
            'Del 1 al 10, ¿qué tan fácil fue contactar a nuestro servicio de atención al cliente?',
            'Del 1 al 10, ¿qué tan bien resolvimos tu consulta o problema?',
            'Del 1 al 10, ¿qué tan rápido fue el tiempo de respuesta de nuestro equipo de atención al cliente?'
        ]

        preguntasRandom = preguntasRandomBool + preguntasRandomNros

        rtaPosibleadhoc = RespuestaPosible.adhoc()

        preguntas = cantidadPreguntas * [None]

        for i in range(cantidadPreguntas):
            preguntaRandom = random.choice(preguntasRandom)
            preguntasRandom.remove(preguntaRandom) # Para que no se repita la pregunta

            for preguntaBool in preguntasRandomBool:
                if preguntaRandom == preguntaBool:
                    respuestas = rtaPosibleadhoc.generarRespuestasSiNo()
            for preguntaNumerica in preguntasRandomNros:
                if preguntaRandom == preguntaNumerica:
                    respuestas = rtaPosibleadhoc.generarRespuestas1Al10()

            preguntas[i] = Pregunta(preguntaRandom, respuestas)
        
        return preguntas


def test():
    n = int(input('Ingrese la cantidad de preguntas a generar (2 o 3): '))
    while n < 2 or n > 3:
        n = int(input('Ingrese la cantidad de preguntas a generar (2 o 3): '))
    
    preguntas = adhoc.generarPreguntasAleatorias(n)
    print('----Preguntas----')
    for i in range(n):
        print('Pregunta:', i + 1)
        print('Descripción:', preguntas[i].pregunta)
        print('Respuestas posibles:', preguntas[i].listarRespuestasPosibles())
        print('---------------------------------')
        #print(preguntas.m_respuestaPosible.getDescripcionRta(preguntas[i].m_respuestaPosible[0]))

if __name__ == '__main__':
    test()
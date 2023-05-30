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
            respuestasPosibles.append(str(self.respuestas[i].getValorRta()))
        return respuestasPosibles
    
    def getRtas(self):
        return self.respuestas

    def __str__(self):
        r = ''
        r += '{:<50}\n'.format('Descripción de la pregunta: ' + self.pregunta)
        respuestasPosibles = self.listarRespuestasPosibles()
        r += 'Respuestas posibles: '
        for respuestaPosible in respuestasPosibles:
            r += '{} '.format(respuestaPosible)
        return r

class adhoc:
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
    
    def __init__(self, respuestasPosibles = RespuestaPosible.adhoc()):
        self.respuestasPosibles = respuestasPosibles
        self.preguntas = self.generarPreguntas()

    def generarPreguntas(self):
        preguntas = []
        for pregunta in self.preguntasRandomBool:
            respuestas = self.respuestasPosibles.getRtasSiNo()
            preguntas.append(Pregunta(pregunta, respuestas))
        for pregunta in self.preguntasRandomNros:
            respuestas = self.respuestasPosibles.getRtas1Al10()
            preguntas.append(Pregunta(pregunta, respuestas))

        return preguntas

    def obtenerPreguntasAleatorias(self, cantidadPreguntas):
        preguntas = cantidadPreguntas * [None]

        for i in range(cantidadPreguntas):
            preguntaRandom = random.choice(self.preguntas)
            while preguntaRandom in preguntas:
                preguntaRandom = random.choice(self.preguntas)
            preguntas[i] = preguntaRandom

            for preguntaBool in preguntasRandomBool:
                if preguntaRandom == preguntaBool:
                    respuestas = adhocRespuestaPosible.getRtasSiNo()
            for preguntaNumerica in preguntasRandomNros:
                if preguntaRandom == preguntaNumerica:
                    respuestas = adhocRespuestaPosible.getRtas1Al10()

            preguntas[i] = Pregunta(preguntaRandom, respuestas)
            
        return preguntas


def test():
    n = int(input('Ingrese la cantidad de preguntas a generar (2 o 3): '))
    while n < 2 or n > 3:
        n = int(input('Ingrese la cantidad de preguntas a generar (2 o 3): '))
    
    preguntas = adhoc().obtenerPreguntasAleatorias(n)
    print('----Preguntas----')
    for i in range(n):
        print(preguntas[i])
        print('---------------------------------')

if __name__ == '__main__':
    test()
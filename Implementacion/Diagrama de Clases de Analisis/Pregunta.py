
import RespuestaPosible

class Pregunta:
    def __init__(self, preg='', resp=RespuestaPosible()):
        self.pregunta = preg
        self.m_respuestaPosible = resp

    def getDescripcion():
        pass

    def listarRespuestasPosibles():
        pass

preguntasRandom = {
    1: ['¿Le gustó la atención?', [self.m_respuestaPosible[0], self.m_respuestaPosible[1]]],
    2: ['¿Del 1 al 10 en cuánto nos calificaría?', []],
    3: ['¿Nos recomendaría a otras personas?', []]
}


def generarPreguntasAleatorias(cantidadPreguntas):
    for i in range(cantidadPreguntas):
        preguntas[i] = Pregunta()
        preguntas[i].pregunta = preguntasRandom[i]
        preguntas[i].m_respuestaPosible = RespuestaPosible.generarRespuestaPosibleAleatoria(cantidadPreguntas)
    
    print('Preguntas generadas con exito')

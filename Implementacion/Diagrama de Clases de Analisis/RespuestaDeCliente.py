
import RespuestaPosible
import FechaYHora
import random

class RespuestaDeCliente:
    def __init__(self, fechaEncuesta='', respuestaSeleccionada=None):
        self.fechaEncuesta = fechaEncuesta
        self.m_respuestaSeleccionada = respuestaSeleccionada

    def getDescripcionRta(self):
        return self.descripcion
    
    def __str__(self):
        r = ''
        r += '{:<30}'.format('Fecha de la Encuesta: ' + str(self.fechaEncuesta))
        return r

class adhoc:
    def generarRtasCliente(self, fechaEncuesta, encuesta):
        rtasPosibles = []
        rtasGeneradas = []
        for pregunta in encuesta.getPreguntas():
            for rtaPosible in pregunta.getRtas():
                rtasPosibles.append(rtaPosible)
            rtasGeneradas.append(random.choice(rtasPosibles))
            rtasPosibles = []
        
        rtasDeCliente = []
        for rtaGenerada in rtasGeneradas:
            rtasDeCliente.append(RespuestaDeCliente(fechaEncuesta, rtaGenerada))
        return rtasDeCliente

def test():
    pass

if __name__ == '__main__':
    test()
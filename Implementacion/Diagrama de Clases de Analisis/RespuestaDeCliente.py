
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
    def generarRtaCliente(self, n):
        respuestas = []
        for i in range(n):
            fechaEncuesta = FechaYHora.obtenerFechaHoraRandom()
            #respuestaSeleccionada = random.choice(RespuestaPosible.)

def main():
    n = 3
    adhocRespuestaPosible = adhoc()
    respuestasGeneradas = adhocRespuestaPosible.generarRespuestas(n, 0)
    adhocRespuestaPosible.mostrar(respuestasGeneradas)

if __name__ == '__main__':
    main()
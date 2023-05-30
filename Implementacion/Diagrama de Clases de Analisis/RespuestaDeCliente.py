
import RespuestaPosible

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
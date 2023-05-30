import random
from datetime import datetime, timedelta

import Cliente
import CambioEstado
import RespuestaDeCliente

class Llamada:
    def __init__(
            self, descripcionOperador, detalleAccionRequerida, encuestaEnviada, observacionAuditor,
            respuestasDeEncuesta = None, cambiosEstado = None, cliente = None):
        self.descripcionOperador  = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.encuestaEnviada = encuestaEnviada
        self.observacionAuditor = observacionAuditor

        self.respuestasDeEncuesta = respuestasDeEncuesta
        self.cambiosEstado = cambiosEstado
        self.cliente = cliente

        self.duracion = self.calcularDuracion()
    
    def calcularDuracion(self):
        cambioEstadoIniciada = None
        cambioEstadoFinalizada = None

        for i in range(len(self.cambiosEstado)):
            if self.cambiosEstado[i].esEstadoInicial():
                cambioEstadoIniciada = self.cambiosEstado[i]
            elif self.cambiosEstado[i].esUltimoEstado():
                cambioEstadoFinalizada = self.cambiosEstado[i]

        duracion = cambioEstadoFinalizada.getFechaHoraInicio() - cambioEstadoIniciada.getFechaHoraInicio()

        return duracion

    def esDePeriodo(self, fechaInicio, fechaFin):
        pass

    def getDuracion(self):
        return self.duracion

    def getNombreClienteDeLlamada(self):
        return self.cliente.getNombre()
    
    def getRespuestas(self):
        pass

    def setDescripcionOperador(self):
        pass

    def setDuracion(self):
        pass

    def setEstadoActual(self):
        pass

    def tieneRta(self):
        pass

    def getLlamada(self):
        return self

    def getEstadoActual():
        pass

    def __str__(self):
        r = ''
        r += '{:<50}'.format('Descripción del operador: ' + self.descripcionOperador + '\n')
        r += '{:<50}'.format('Acción requerida: ' + self.detalleAccionRequerida)
        r += '{:<40}'.format('Duración de la llamada: ' + str(self.duracion))
        r += '{:<30}'.format('Encuesta Enviada: ' + str(self.encuestaEnviada))
        r += '{:<40}'.format('Observación del Auditor: ' + str(self.observacionAuditor))
        return r

class adhoc:
    def generarLlamadaRandom(self):
        desc = ['Ofrecimiento de reembolso o crédito para compensar cualquier cargo adicional.',
                'Asistencia técnica para resolver problemas de velocidad de conexión.',
                'Aclaración de las políticas de cancelación', 'Aclaración de las políticas de de cambio de servicio.',
                'Actualización de servicios.']
        accionreq = ['Comunicar saldo.', 'Dar de baja tarjeta.', 'Denunciar un robo.']
        observAudi = ['Ninguna.', 'Incorrecto trato del operador al cliente.', 'Voz poco clara del operador.',
                      'El operador se demoró.', 'La respuesta que el operador brindó no resolvió el problema del cliente.']
        
        descripcionOperadorRandom = random.choice(desc)
        detalleAccionRequeridaRandom = random.choice(accionreq)
        duracion = [random.randint(1, 20), random.randint(1, 60)]
        encuestaEnviada = bool(random.getrandbits(1))
        observacionAuditor = random.choice(observAudi)

        clienteRandom = Cliente.adhoc().obtenerClienteRandom()

        cambiosEstadoRandom = CambioEstado.adhoc().obtenerCambiosEstado(index = random.randint(0, 3))

        llamadaRandom = Llamada(
            descripcionOperadorRandom, detalleAccionRequeridaRandom, encuestaEnviada, observacionAuditor,
            cliente = clienteRandom, cambiosEstado = cambiosEstadoRandom)

        return llamadaRandom

def test():
    adhocLlamadas = adhoc()
    for i in range(5):
        print()
        llamadaRandom = adhocLlamadas.generarLlamadaRandom()
        print(llamadaRandom)

if __name__ == '__main__':
    test()

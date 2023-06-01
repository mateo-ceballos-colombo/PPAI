import random
from datetime import datetime, timedelta

import Cliente
import CambioEstado
import RespuestaDeCliente
import Encuesta

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
    
    def getEncuestaEnviada(self):
        return self.encuestaEnviada

    # Cálculo de la duración de la llamada a través de Cambio de Estado
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
        for cambioEstado in self.cambiosEstado:
            if cambioEstado.esEstadoInicial():
                fechaHoraInicio = cambioEstado.getFechaHoraInicio()

        if fechaInicio <= fechaHoraInicio <= fechaFin:
            return True
        return False
    
    def obtenerFechaHoraInicio(self):
        for cambioEstado in self.cambiosEstado:
            if cambioEstado.esEstadoInicial():
                return cambioEstado.getFechaHoraInicio()

    def getDuracion(self):
        return self.duracion

    def getNombreClienteDeLlamada(self):
        return self.cliente.getNombre()
    
    def getRespuestas(self):
        return self.respuestasDeEncuesta

    # Métodos que no usamos ---------
    def setDescripcionOperador(self):
        pass

    def setDuracion(self):
        pass

    def setEstadoActual(self):
        pass

    def tieneRta(self):
        pass
    # -------------------------------
    
    def getLlamada(self):
        return self

    def getEstadoActual(self):
        for i in range(len(self.cambiosEstado)):
            if self.cambiosEstado[i].esUltimoEstado():
                return self.cambiosEstado[i].getNombreEstado()

    def __str__(self):
        r = ''
        r += '{:<50}'.format('Descripción del operador: ' + self.descripcionOperador + '\n')
        r += '{:<50}'.format('Acción requerida: ' + self.detalleAccionRequerida)
        r += '{:<40}'.format('Duración de la llamada: ' + str(self.duracion))
        r += '{:<30}'.format('Encuesta Enviada: ' + str(self.encuestaEnviada))
        r += '{:<40}'.format('Observación del Auditor: ' + str(self.observacionAuditor))
        return r

class adhoc:
    def __init__(self):
        pass

    def generarLlamadaRandom(self, encuesta = Encuesta.adhoc().generarEncuestasAleatorias(1)[0]):
        desc = ['Ofrecimiento de reembolso o crédito para compensar cualquier cargo adicional.',
                'Asistencia técnica para resolver problemas de velocidad de conexión.',
                'Aclaración de las políticas de cancelación', 'Aclaración de las políticas de cambio de servicio.',
                'Actualización de servicios.']
        accionreq = ['Comunicar saldo.', 'Dar de baja tarjeta.', 'Denunciar un robo.']
        observAudi = ['Ninguna.', 'Incorrecto trato del operador al cliente.', 'Voz poco clara del operador.',
                      'El operador se demoró.', 'La respuesta que el operador brindó no resolvió el problema del cliente.']
        
        descripcionOperadorRandom = random.choice(desc)
        detalleAccionRequeridaRandom = random.choice(accionreq)
        encuestaEnviada = True
        observacionAuditor = random.choice(observAudi)
        clienteRandom = Cliente.adhoc().obtenerClienteRandom()
        
        # Generar llamadas que sólo pasan por los estados de Iniciada -> Finalizada o Iniciada ->  
        cambiosEstadoRandom = CambioEstado.adhoc().obtenerCambiosEstado(index = random.randint(0, 1))

        fechaHoraFin = datetime.now()
        for cambioEstado in cambiosEstadoRandom:
            if cambioEstado.esUltimoEstado():
                fechaHoraFin = cambioEstado.getFechaHoraFin()
        rtasDeCliente = RespuestaDeCliente.adhoc().generarRtasCliente(fechaHoraFin, encuesta)
        

        # Creo el objeto Llamada 
        llamadaRandom = Llamada(
            descripcionOperadorRandom, detalleAccionRequeridaRandom, encuestaEnviada, observacionAuditor,
            respuestasDeEncuesta = rtasDeCliente, cliente = clienteRandom, cambiosEstado = cambiosEstadoRandom)

        return llamadaRandom

def test():
    adhocLlamadas = adhoc()
    for i in range(5):
        print()
        llamadaRandom = adhocLlamadas.generarLlamadaRandom()
        print(llamadaRandom)

if __name__ == '__main__':
    test()

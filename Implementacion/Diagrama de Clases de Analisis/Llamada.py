import random
from Cliente import Cliente, adhoc
import datetime as dt
import GestorConsultarEncuesta as gestor

class Llamada:
    def __init__(self, descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor):
        self.descripcionOperador  = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.observacionAuditor = observacionAuditor
    
    def calcularDuracion(self):
        pass

    def esDePeriodo(self, fechaInicio, fechaFin):
        #g = ''
        #fecha_actual = dt.datetime.now()
        #if fecha_actual >= fechaInicio and fecha_actual <= fechaFin:
        #    return True
        pass

    def getDuracion(self):
        return self.duracion

    def getNombreClienteDeLlamada(self):
        cliente = Cliente()
        return cliente.getNombre()

    def new(self):
        llamada = [None]
        generarLlamadas(llamada, 1)
        return llamada

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

def generarLlamadas(v, n):
    desc = ['Ofrecimiento de reembolso o crédito para compensar cualquier cargo adicional.',
            'Asistencia técnica para resolver problemas de velocidad de conexión.',
            'Aclaración de las políticas de cancelación', 'Aclaración de las políticas de de cambio de servicio.',
            'Actualización de servicios.']
    accionreq = ['Comunicar saldo.', 'Dar de baja tarjeta.', 'Denunciar un robo.']
    observAudi = ['Ninguna.', 'Incorrecto trato del operador al cliente.', 'Voz poco clara del operador.',
                  'El operador se demoró.', 'La respuesta que el operador brindó no resolvió el problema del cliente.'
                  ]
    for i in range(n):
        descripcionOperador = random.choice(desc)
        detalleAccionRequerida = random.choice(accionreq)
        duracion = [random.randint(1, 20), random.randint(1, 60)]
        encuestaEnviada = bool(random.getrandbits(1))
        observacionAuditor = random.choice(observAudi)

        col = Llamada(descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor)
        v.append(col)

def write(col):
    print('')
    print('Descripción del operador: ' + col.descripcionOperador + '\t')
    print('Acción requerida: ' + col.detalleAccionRequerida + '\t')
    print('Duración de la llamada : ' + str(col.duracion[0]) + ' minutos con ' + str(col.duracion[1]) + ' segundos.' + '\t')
    print('Encuesta Enviada: ' + str(col.encuestaEnviada) + '\t')
    print('Observación del Auditor:' + col.observacionAuditor + '\t')
    print('')

def mostrar(vector):
    for i in range(len(vector)):
        write(vector[i])


if __name__ == '__main__':
    n = 10
    llamadasDefinidas = []
    generarLlamadas(llamadasDefinidas, n)
    mostrar(llamadasDefinidas)
    #Llamada.getNombreClienteDeLlamada(llamadasDefinidas[0])

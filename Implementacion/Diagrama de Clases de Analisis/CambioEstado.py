import Estado
from datetime import datetime, timedelta
import random

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado

    def esEstadoInicial(self):
        return self.estado.esIniciada()

    def esUltimoEstado(self):
        if self.fechaHoraFin is None:
            return True
        return False

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio
    
    def getFechaHoraFin(self):
        return self.fechaHoraFin

    def getNombreEstado(self):
        return self.estado.getNombre()
    
    def getEstado(self):
        return self.estado
    
    def __str__(self):
        r = ''
        r += '{:<50}'.format("Fecha y Hora de Inicio: " + self.fechaHoraInicio.strftime("%d/%m/%Y %H:%M:%S"))
        r += '{:<50}'.format("Fecha y Hora de Fin: " + 
            (self.fechaHoraFin.strftime("%d/%m/%Y %H:%M:%S") if self.fechaHoraFin is not None else "No tiene"))
        r += '{:<40}'.format("Estado: " + self.estado.getNombre())
        return r

class adhoc:
    def obtenerFechaHoraRandom(self, startDate = datetime(day=1,month=1,year=1990), endDate = datetime(day=1,month=1,year=2022)):
        # Calcular el rango de fechas
        dateRange = endDate - startDate

        # Generar un numero aleatorio en el rango
        randomDays = random.randint(0, dateRange.days)

        # Agregar el numero aleatorio de dias
        randomDate = startDate + timedelta(days = randomDays)

        # Agregar hora, minutos y segundos random
        randomDate = randomDate + timedelta(seconds=random.randint(1, 59), minutes=random.randint(1, 59), hours=random.randint(1, 23))

        return randomDate
    
    def obtenerCambiosEstado(self, index = 0):
        # El index representa cual de las combinaciones posibles de cambio de estado se usara segun la maquina de estados
        # 0: Iniciada -> Finalizada
        # 1: Iniciada -> En Curso -> Finalizada
        # 2: Iniciada -> Cancelada
        # 3: Iniciada -> En Curso -> Cancelada

        adhocEstado = Estado.adhoc()
        fechaHoraInicioRandom = self.obtenerFechaHoraRandom()

        cambioEstadoIniciada = CambioEstado(
                fechaHoraInicioRandom, 
                fechaHoraInicioRandom + timedelta(minutes = random.randint(1, 15), seconds=random.randint(1, 59)),
                adhocEstado.obtenerEstados()[0]
            )
        
        if index == 0:
            cambioEstadoFinalizada = CambioEstado(
                cambioEstadoIniciada.getFechaHoraFin(),
                None,
                adhocEstado.obtenerEstados()[2]
            )
            return [cambioEstadoIniciada, cambioEstadoFinalizada]
        elif index == 1:
            cambioEstadoEnCurso = CambioEstado(
                cambioEstadoIniciada.getFechaHoraFin(),
                cambioEstadoIniciada.getFechaHoraFin() + timedelta(minutes = random.randint(1, 15), seconds=random.randint(1, 59)),
                adhocEstado.obtenerEstados()[1]
            )
            cambioEstadoFinalizada = CambioEstado(
                cambioEstadoEnCurso.getFechaHoraFin(),
                None,
                adhocEstado.obtenerEstados()[2]
            )
            return [cambioEstadoIniciada, cambioEstadoEnCurso, cambioEstadoFinalizada]
        elif index == 2:
            cambioEstadoCancelada = CambioEstado(
                cambioEstadoIniciada.getFechaHoraFin(),
                None,
                adhocEstado.obtenerEstados()[3]
            )
            return [cambioEstadoIniciada, cambioEstadoCancelada]
        elif index == 3:
            cambioEstadoEnCurso = CambioEstado(
                cambioEstadoIniciada.getFechaHoraFin(),
                cambioEstadoIniciada.getFechaHoraFin() + timedelta(minutes = random.randint(1, 15), seconds=random.randint(1, 59)),
                adhocEstado.obtenerEstados()[1]
            )
            cambioEstadoCancelada = CambioEstado(
                cambioEstadoEnCurso.getFechaHoraFin(),
                None,
                adhocEstado.obtenerEstados()[3]
            )
            return [cambioEstadoIniciada, cambioEstadoEnCurso, cambioEstadoCancelada]
    
def test():
    adhocCambioEstado = adhoc()
    for i in range(4):
        print()
        cambiosEstado = adhocCambioEstado.obtenerCambiosEstado(i)
        for i in range(len(cambiosEstado)):
            print(cambiosEstado[i])

if __name__ == "__main__":
    test()
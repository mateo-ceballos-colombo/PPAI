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

    def getNombreEstado(self):
        return self.estado.getNombre()
    
    def __str__(self):
        r = ''
        r += '{:<40}'.format("Fecha y Hora de Inicio: " + self.fechaHoraInicio.strftime("%d/%m/%Y"))
        r += '{:<40}'.format("Fecha y Hora de Fin: " + 
            (self.fechaHoraFin.strftime("%d/%m/%Y") if self.fechaHoraFin is not None else "No tiene"))
        r += '{:<40}'.format("Estado: " + self.estado.getNombre())
        return r

class adhoc:
    def obtenerFechaRandom(self, start_date, end_date):
        # Convertir las fechas de inicio y fin de string a datetime
        startDatetime = datetime.strptime(start_date, "%d/%m/%Y")
        endDatetime = datetime.strptime(end_date, "%d/%m/%Y")

        # Calculate the range of dates
        dateRange = endDatetime - startDatetime

        # Generate a random number of days within the range
        randomDays = random.randint(0, dateRange.days)

        # Add the random number of days to the start date
        randomDate = startDatetime + timedelta(days = randomDays)

        return randomDate

    # Crea un cambio de estado. Si es ultimo estado, no tiene fecha de fin
    def crearCambioEstado(self, esUltimoestado):
        fechaRandomInicio = self.obtenerFechaRandom("01/01/1900", "31/12/2022")
        

        adhocEstado = Estado.adhoc()

        estado = adhocEstado.obtenerEstado()

        if esUltimoestado:
            fechaRandomFin = None
        else:
            fechaRandomFin = self.obtenerFechaRandom("01/01/1900", "31/12/2022")
            while fechaRandomFin < fechaRandomInicio:
                fechaRandomFin = self.obtenerFechaRandom("01/01/1900", "31/12/2022")
        
        cambioEstado = CambioEstado(fechaRandomInicio, fechaRandomFin, estado)
        return cambioEstado
    
def test():
    adhocCambioEstado = adhoc()
    vec = []
    for i in range(5):
        estados = [True, False]
        selec = random.choice(estados)
        cm = adhocCambioEstado.crearCambioEstado(selec)
        vec.append(cm)

        print(vec[i])
        print("Es ultimo estado:", vec[i].esUltimoEstado())
    

if __name__ == "__main__":
    test()
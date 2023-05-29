import random

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

    def esFinalizada(self):
        if self.nombre == 'Finalizada':
            return True
        return False

    def esIniciada(self):
        if self.nombre == 'Iniciada':
            return True
        return False
    
    def getNombre(self):
        return self.nombre
    
    def __str__(self):
        r = ''
        r += '{:<30}'.format("Nombre Estado: " + str(self.nombre))
        return r


class adhoc:
    def obtenerEstado(self):
        arrayEstados = ['Iniciada', 'En Curso', 'Finalizada', 'Cancelada']
        nombre = random.choice(arrayEstados)
        estado = Estado(nombre)
        return estado
        
def test(self):
    estado = adhoc().obtenerEstado()
    print(estado)
    print("Get nombre:", estado.getNombre())
    print("Es finalizada:", estado.esFinalizada())
    print("Es iniciada:", estado.esIniciada())


if __name__ == "__main__":
    test()

import random

class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

    def esCliente(self):
        return True

    def getNombre(self):
        return self.nombreCompleto
    
    def __str__(self):
        r = ''
        r += '{:<40}'.format("DNI: " + str(self.dni))
        r += '{:<40}'.format("Nombre y Apellido: " + self.nombreCompleto)
        r += '{:<40}'.format("Numero celular: " + str(self.nroCelular))
        return r


class adhoc:
    def crearClientes(n):
        descNombres = ["Juan","Joaquin","Fabrizio", "Luciana","Matias","Mateo","Federico",
            "Santiago","Lucia","Valentina","Victoria", "Ana", "María","Pedro","Josefina",
            "Jose","Lucio","Patricia","Natalia"]
        descApellidos = ["Sposetti","Gonzalez", "Rodriguez", "Lopez", "Martinez", 
            "Perez", "Gomez", "Sanchez", "Fernandez", "Torres", "Ramirez", "Hernandez", 
            "Garcia", "Silva", "Rojas", "Moreno", "Navarro", "Cruz", "Ortega", "Vargas", "Mendoza"]
        
        vecClientes = []
        for i in range(n):
            dni = random.randint(100000, 46000000)
            nombreCompleto = random.choice(descNombres) + " " + random.choice(descApellidos)
            nroCelular = random.randint(540000000000, 550000000000)
            cliente = Cliente(dni, nombreCompleto, nroCelular)
            vecClientes.append(cliente)

        return vecClientes


def test():
    clientes = adhoc.crearClientes(10)
    for i in range(10):
        print(clientes[i])
        print("Get nombre: ", clientes[i].getNombre())


if __name__ == "__main__":
    test()
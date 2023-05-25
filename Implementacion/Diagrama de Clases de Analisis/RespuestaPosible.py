import random
import RespuestaPosible

class RespuestaPosible:
    def __init__(self, des='', val=''):
        self.descripcion = des
        self.valor = val

    def getDescripcionRta():
        return self.des

# ~La clase adhoc es una clase auxiliar que se utiliza para generar respuestas posibles aleatorias
# ~para las preguntas de la encuesta
class adhoc:
    def generarRespuestas(v, n):
        descripcionesGenerales = ['1 al 10', 'Si/No']
        valoresGenerales = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Si', 'No']]
        for i in range(n):
            descripcion = random.choice(descripcionesGenerales)
            if descripcion == descripcionesGenerales[0]:
                valoresGenerales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                valor = random.choice(valoresGenerales)
            else:
                valoresGenerales = ['Si', 'No']
                valor = random.choice(valoresGenerales)
       
            v[i] = RespuestaPosible(descripcion, valor)


def string(col):
    print('Descripción de la respuesta: ', col.descripcion)
    print('Valor de la respuesta:', str(col.valor))
    print('')
    
def mostrar(vector):
    print('----Respuestas posibles----')
    for i in range(len(vector)):
        print('Respuesta ', i + 1)
        string(vector[i])

def main():
    n = 3
    RespuestasDefinidas = n * [None]
    adhoc.generarRespuestas(RespuestasDefinidas, n)
    mostrar(RespuestasDefinidas)

if __name__ == '__main__':
    main()
import random


class RespuestaPosible:
    def __init__(self, des='', val=''):
        self.descripcion = des
        self.valor = val

    def getDescripcionRta():
        return self.des

# ~La clase adhoc es una clase auxiliar que se utiliza para generar respuestas posibles aleatorias
# ~para las preguntas de la encuesta
class adhoc:
    def generarRespuestas(n, tipoPregunta):
        descripcionesGenerales = ['1 al 10', 'Si/No']
        valoresGenerales = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Si', 'No']]
        respuestas = []
        for _ in range(n):
            if tipoPregunta == 1:
                descripcion = descripcionesGenerales[0]
                valor = random.choice(valoresGenerales[0])
            elif tipoPregunta == 2:
                descripcion = descripcionesGenerales[1]
                valor = random.choice(valoresGenerales[1])
            respuestas.append(RespuestaPosible(descripcion, valor))
        return respuestas

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
    
    adhoc.generarRespuestas(n, tipoPregunta)
    mostrar(RespuestasDefinidas)

if __name__ == '__main__':
    main()
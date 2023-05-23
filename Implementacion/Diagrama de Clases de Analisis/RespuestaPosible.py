descripcionesGenerales = ['1 al 10', 'Si/No']
valoresGenerales = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Si', 'No']]

class RespuestaPosible:
    def init(self, des='', val=''):
        self.descripcion = des
        self.valor = val

    def getDescripcionRta():
        return self.des

import random

descripcionesGenerales = ['1 al 10', 'Si/No']
valoresGenerales = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Si', 'No']]

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

            col = RespuestaPosible(descripcion, valor)
            v.append(col)

def str(col):
    print('')
    print('Descripción de la pregunta: ' + col.descripcion + '\t')
    print('Valor de la pregunta:' + str(col.valor) + '\t')
    print('')

def mostrar(vector):
    for i in range(len(vector)):
        str(vector[i])

def main(): 
    n = 3
    RespuestasDefinidas = []
    adhoc.generarRespuestas(RespuestasDefinidas, n)
    mostrar(RespuestasDefinidas)

if name == 'main':
    main()
import random

class RespuestaPosible:
    def __init__(self, des='', val=''):
        self.descripcion = des
        self.valor = val

    def getDescripcionRta(self):
        return self.descripcion
    
    def __str__(self):
        r = ''
        r += '{:<50}'.format('Descripción de la respuesta: ' + self.descripcion)
        r += '{:<30}'.format('Valor de la respuesta: ' + str(self.valor))
        return r

# La clase adhoc es una clase auxiliar que se utiliza para generar respuestas posibles aleatorias
# para las preguntas de la encuesta
class adhoc:
    def generarRespuestas(self, n, tipoPregunta):
        descripcionesGenerales = ['1 al 10', 'Si/No']
        valoresGenerales = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Si', 'No']]
        respuestas = []
        for i in range(n):
            descripcion = descripcionesGenerales[tipoPregunta]
            valor = random.choice(valoresGenerales[tipoPregunta])

            respuestas.append(RespuestaPosible(descripcion, valor))

        return respuestas

    def mostrar(self, vector):
        print('----Respuestas posibles----')
        for i in range(len(vector)):
            print('Respuesta', i + 1)
            print(vector[i])

def main():
    n = 3
    adhocRespuestaPosible = adhoc()
    respuestasGeneradas = adhocRespuestaPosible.generarRespuestas(n, 0)
    adhocRespuestaPosible.mostrar(respuestasGeneradas)

if __name__ == '__main__':
    main()
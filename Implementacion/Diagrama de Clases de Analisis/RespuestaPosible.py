import random

class RespuestaPosible:
    def __init__(self, des='', val=''):
        self.descripcion = des
        self.valor = val

    def getDescripcionRta(self):
        return self.descripcion
    
    def getValorRta(self):
        return self.valor
    
    def __str__(self):
        r = ''
        r += '{:<50}'.format('Descripción de la respuesta: ' + self.descripcion)
        r += '{:<30}'.format('Valor de la respuesta: ' + str(self.valor))
        return r

# La clase adhoc es una clase auxiliar que se utiliza para generar respuestas posibles aleatorias
# para las preguntas de la encuesta
class adhoc:
    def generarRespuestas1Al10(self):
        descrip = '1 al 10'
        rtasPosibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        respuestas = []
        for rtaPosible in rtasPosibles:
            respuestas.append(RespuestaPosible(descrip, rtaPosible))

        return respuestas
    
    def generarRespuestasSiNo(self):
        descrip = 'Si/No'
        rtas = ['Si', 'No']
        respuestas = []
        for rta in rtas:
            respuestas.append(RespuestaPosible(descrip, rta))
        
        return respuestas

def main():
    adhocRespuestaPosible = adhoc()

    rtas1Al10 = adhocRespuestaPosible.generarRespuestas1Al10()
    for rta1Al10 in rtas1Al10:
        print(rta1Al10)
    rtasSiNo = adhocRespuestaPosible.generarRespuestasSiNo()
    for rtaSiNo in rtasSiNo:
        print(rtaSiNo)

if __name__ == '__main__':
    main()
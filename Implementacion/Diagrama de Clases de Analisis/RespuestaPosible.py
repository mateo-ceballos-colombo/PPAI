#######################################################
# 
# RespuestaPosible.py
# Python implementation of the Class RespuestaPosible
# Generated by Enterprise Architect
# Created on:      11-may.-2023 16:25:04
# Original author: usuario
# 
#######################################################

# '# ~Comment' code convention by Cocimano Federico Jose
# ~Changes:
#~ Construnctor de la clase RespuestaPosible

descripcionesGenerales = ['1 al 10', 'Si/No']
valoresGenerales = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Si', 'No']]


class RespuestaPosible:
    def __init__(self, des='', val=''):
        self.descripcion = des
        self.valor = val

    def getDescripcionRta():
        pass

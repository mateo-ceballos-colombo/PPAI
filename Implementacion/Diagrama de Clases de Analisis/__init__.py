import os
import random

import PantallaConsultarEncuesta
import GestorConsultarEncuesta
import Llamada
import Encuesta
import Pregunta
import RespuestaPosible

def main():
    # os.system('cls')

    adhocRtasPosibles = RespuestaPosible.adhoc()
    adhocPreguntas = Pregunta.adhoc(adhocRtasPosibles)
    adhocEncuestas = Encuesta.adhoc(adhocPreguntas)
    encuestasRandom = adhocEncuestas.generarEncuestasAleatorias(5)

    adhocLlamadas = Llamada.adhoc()
    llamadasRandom = []
    for i in range(5):
        llamadaRandom = adhocLlamadas.generarLlamadaRandom(encuestasRandom[i])
        llamadasRandom.append(llamadaRandom)

    pantalla = PantallaConsultarEncuesta.PantallaConsultarEncuesta()
    gestor = GestorConsultarEncuesta.GestorConsultarEncuesta(llamadas = llamadasRandom, encuestas = encuestasRandom)

    pantalla.setGestor(gestor)
    gestor.setPantalla(pantalla)

    pantalla.opcionConsultarEncuesta(gestor)

if __name__ == "__main__":
    main()


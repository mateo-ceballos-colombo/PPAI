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
    encuestasRandom = adhocEncuestas.generarEncuestasAleatorias(10)

    adhocLlamadas = Llamada.adhoc(encuestasRandom[random.randint(0, 9)])
    llamadasRandom = []
    for i in range(100):
        llamadaRandom = adhocLlamadas.generarLlamadaRandom()
        llamadasRandom.append(llamadaRandom)


    pantalla = PantallaConsultarEncuesta.PantallaConsultarEncuesta()
    gestor = GestorConsultarEncuesta.GestorConsultarEncuesta(llamadas = llamadasRandom)

    pantalla.setGestor(gestor)
    gestor.setPantalla(pantalla)

    pantalla.opcionConsultarEncuesta(gestor)

if __name__ == "__main__":
    main()


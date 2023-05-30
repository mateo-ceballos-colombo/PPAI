import os

import PantallaConsultarEncuesta
import GestorConsultarEncuesta
import Llamada
import Encuesta

def main():
    # os.system('cls')

    adhocLlamadas = Llamada.adhoc()
    llamadasRandom = []
    for i in range(50):
        llamadaRandom = adhocLlamadas.generarLlamadaRandom()
        llamadasRandom.append(llamadaRandom)

    pantalla = PantallaConsultarEncuesta.PantallaConsultarEncuesta()
    gestor = GestorConsultarEncuesta.GestorConsultarEncuesta(llamadas = llamadasRandom)

    pantalla.setGestor(gestor)
    gestor.setPantalla(pantalla)

    pantalla.opcionConsultarEncuesta(gestor)

if __name__ == "__main__":
    main()


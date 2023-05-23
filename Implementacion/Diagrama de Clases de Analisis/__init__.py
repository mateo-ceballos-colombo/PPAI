import os

import PantallaConsultarEncuesta
import GestorConsultarEncuesta
import Llamada

def main():
    # os.system('cls')
    
    llamadas = []
    Llamada.generarLlamadas(llamadas, 20)

    pantalla = PantallaConsultarEncuesta.PantallaConsultarEncuesta()
    gestor = GestorConsultarEncuesta.GestorConsultarEncuesta(pantalla, llamadas)

    pantalla.opcionConsultarEncuesta(gestor)

if __name__ == "__main__":
    main()


import os

import PantallaConsultarEncuesta
import GestorConsultarEncuesta

def main():
    os.system('cls')
    
    pantalla = PantallaConsultarEncuesta.PantallaConsultarEncuesta()
    gestor = GestorConsultarEncuesta.GestorConsultarEncuesta(pantalla)
    
    pantalla.opcionConsultarEncuesta(gestor)

if __name__ == "__main__":
    main()
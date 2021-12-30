from src.main.scripts.functions import generalFunctions, inOutFunctions
from src.main.scripts.objects.Game import Game
import sys
import logging

if __name__ == '__main__':
    print("Inicio Programa")

    # Preparamos la configuración de "config.ini"
    inOutFunctions.setConfig()

    print(logging.DEBUG)

    logger = generalFunctions.getLogger("MAIN")

    logger.error("Peter")

    g = Game()
    print("Fin Programa")

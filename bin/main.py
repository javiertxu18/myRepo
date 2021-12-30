from src.main.scripts.functions import generalFunctions, inOutFunctions
from src.main.scripts.objects.Game import Game
import sys
import logging

if __name__ == '__main__':
    # Configuración inicial
    inOutFunctions.setConfig()
    logger = generalFunctions.getLogger("MAIN")

    logger.info("Inicio Programa")

    g = Game()

    logger.info("Fin Programa")

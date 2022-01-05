from multipledispatch import dispatch

from src.main.scripts.functions import generalFunctions


class Objective:
    # Constructor
    def __init__(self):
        self.logger = generalFunctions.getLogger("Objective")  # Preparamos el logger
        self._target = ""  # Objetivo
        self._shadow = ""  # Objetivo en asteriscos
        self._tries = 0  # Intentos restantes
        self.__accomplished = False  # Objetivo cumplido

        self._lstIntentosLetras = []  # Intentos de letras
        self._lstIntentosPalabras = []  # Intentos de palabras
        self._lstIntentosFrases = []  # Intentos de frases

    # Getters & Setters
    # Sets the target
    @dispatch(str)
    def _setTarget(self, newTarget):
        self._target = newTarget
        self._setShadow()

    # Gets the target
    def getTarget(self):
        return self._target

    # Sets the shadow (_target covered with asterisks)
    def _setShadow(self):
        for x in self._target:
            if x != " ":
                self._shadow += "*"
            else:
                self._shadow += " "

    # Gets the shadow
    def getShadow(self):
        return self._shadow

    # Sets the tries
    def _setTries(self, tries):
        try:
            self._tries = int(tries)
            return True
        except Exception:
            self._tries = 0
            return False

    # Sets accomplished
    def _setAccomplished(self, val):
        try:
            self.__accomplished = bool(val)
            return True
        except Exception:
            self.__accomplished = False
            return False

    # Gets accomplished
    def getAccomplished(self):
        return self.__accomplished

    # Methods

    # -----------------------------------------------------------------------------------------------
    # DESC:
    #   Devuelve una lista con el target separado por lo introducido en parámetro
    # Params:
    #   separator: separador
    # Return:
    #   list

    def getSplitTarget(self, separator=" "):
        return str(self._target).split(separator)

    # -----------------------------------------------------------------------------------------------
    # DESC:
    #   Devuelve si el usuario ha descifrado toda la frase
    # Params:
    #   none
    # Return:
    #   True si la ha completado
    #   False si no la ha completado

    def isAccomplished(self):
        if self._target == self._shadow:
            self.__accomplished = True
            return self.__accomplished

        return False

    # -----------------------------------------------------------------------------------------------
    # DESC:
    #   Comprueba si la letra pasada por parámetros existe en el target.
    #   En caso de existir, actualiza el shadow
    # Params:
    #   letra
    # Return:
    #   True si existe
    #   False si no existe

    def charExists(self, letra):
        self.logger.debug("Comprobando si la letra existe")
        if len(str(letra)) != 1 or str(letra) == " ":
            self.logger.error("El string insertado está vacío, o es más largo de lo permitido(1).")
            return -1

        found = False
        lstTarget = list(self._target)
        lstShadow = list(self._shadow)

        for x in range(len(lstTarget)):
            if str(letra) == str(lstTarget[x]):
                lstShadow[x] = str(letra)
                found = True

        self._shadow = "".join(lstShadow)

        return found

    # -----------------------------------------------------------------------------------------------
    # DESC:
    #   Comprueba si la palabra pasada por parámetros existe en el target.
    #   En caso de existir, actualiza el shadow
    # Params:
    #   palabra
    # Return:
    #   True si existe
    #   False si no existe

    def wordExists(self, palabra):
        self.logger.debug("Comprobando si la palabra existe")
        tar = self.getSplitTarget(" ")  # Separamos el targen por espacios
        sha = str(self._shadow).split(" ")  # Separamos el shadow por espacios
        dev = False  # Preparamos dev, que es lo que vamos a devolver
        for x in range(len(tar)):
            if str(palabra) == str(tar[x]):
                sha[x] = str(palabra)  # Actualizamos el shadow temporal
                self._shadow = " ".join(sha)  # Actualizamos el shadow del objeto
                dev = True  # Cambiamos dev a true

        return dev  # Retornamos dev

    # -----------------------------------------------------------------------------------------------
    # DESC:
    #   Comprueba si la frase pasada por parámetros existe en el target.
    #   En caso de existir, actualiza el shadow
    # Params:
    #   frase
    # Return:
    #   True si existe
    #   False si no existe

    def sentenceExists(self, frase):
        self.logger.debug("Comprobando si la frase existe")
        if str(frase) == self._target:
            self._shadow = self._target  # Actualizamos el shadow
            return True
        else:
            return False

    # -----------------------------------------------------------------------------------------------

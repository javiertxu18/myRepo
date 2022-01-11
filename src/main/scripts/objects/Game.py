from multipledispatch import dispatch
from src.main.scripts.functions import inOutFunctions, generalFunctions
from src.main.scripts.objects.Objective import Objective
from src.main.scripts.objects.User import User
import pandas as pd


# staticFunctions
def myBreak():
    return -1


class Game(Objective):

    # Constructor
    def __init__(self):
        # Inicializamos la/s clase/s padre/s
        Objective.__init__(self)

        # Creamos los atributos
        self.logger = generalFunctions.getLogger("Game")  # Preparamos el logger
        self.activeUser = User("guest", generalFunctions.encript("1234"))  # El usuario activo
        self.usersFilePath = inOutFunctions.readConfig()["game_files"]["users_path"]  # Ruta al fichero de usuarios
        self.rankingFilePath = inOutFunctions.readConfig()["game_files"]["ranking_path"]  # Ruta al fichero de rankings

    # -----------------------------------------------------------------------------------------------

    # Método para iniciar el juego

    def startMenu(self):
        self.logger.info("Iniciando menú")

        while True:
            print(f"\nBeinvenido/a  {str(self.activeUser.name).capitalize()}")
            print("MENÚ - Adivina la frase")
            print("\n\t1 - Jugar")
            print("\t2 - Ver ranking")
            print("\t3 - Cambiar de usuario")
            print("\t0 - Salir")

            # Comprobamos que el usuario ha insertado un valor válido
            try:
                userOption = int(input("\nOpción: "))

                if userOption < 0 or userOption > 3:
                    raise ValueError("\tValor fuera de límites. Introduzca un valor numérico entre el 0 y el 2.")

            except ValueError as ve:
                print("\n\tValor no válido. Introduzca un valor numérico entre el 0 y el 2.\n")
                self.logger.error(str(ve))
                continue
            except Exception as e:
                print("\n\tError, valor introducido no válido. Introduzca un valor numérico entre el 0 y el 2.\n")
                self.logger.error(str(e))
                continue

            # Alternativa a Switch
            avOpt = {1: self.playGame, 2: self.showRankings, 3: self.changeUserMenu, 0: self.exitMenu}
            result = avOpt.get(userOption, 'Default controlado por excepciones')
            result()

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------

    # Métodos para jugar al juego

    def playGame(self):
        self.logger.info("Jugando juego")
        self.menuJuego()
        self.logger.info("Fin jugando juego")

    # Menú juego
    def menuJuego(self):

        while True:
            print("\nJUEGO - Adivina la frase\n\n\t1 - Jugar\n\t2 - Ver instrucciones\n\t0 - Volver a menú principal")
            try:
                opUser = int(input("\nOpción: "))

                if opUser < 0 or opUser > 2:
                    raise Exception

            except Exception:
                print("\n\tError, introduzca un número entre el 0 y el 2.\n")
                continue
            avOp = {0: myBreak, 1: self.play, 2: self.instr}
            result = avOp.get(opUser, "Default controlado por excepciones")

            if result() == -1:
                break

    # -----------------------------------------------------------------------------------------------

    # Jugar al juego

    def play(self):
        self.logger.info("Jugando al juego.")

        print("\n\tConfiguración del juego.")

        # Preparamos la frase objetivo
        self.logger.debug("Preparamos el target")
        self._setTarget(str(input("\n\tAdmin, introduzca la frase a adivinar: ")))

        # Definimos el número de intentos
        self.logger.debug("Definimos el número de intentos.")
        self._setTries(int(input("\tInserte el número de intentos disponibles: ")))

        # Empezamos a jugar
        print("\n\tComenzando juego.")

        # El bucle continuará mientras queden intentos y no esté solucionada la frase
        self.logger.debug("Iniciando fase 1 de juego.")
        while self._tries > 0 and not self.isAccomplished():
            txt = "\tJugador, inserte el número de palabras que cree que contiene la frase: "
            num = int(input(txt))
            if num == len(self.getSplitTarget()):
                print(f"\n\tCorrecto, la frase contiene {len(self.getSplitTarget())} "
                      f"palabras. Le quedan {self._tries} intentos.\n")
                break
            elif num > len(self.getSplitTarget()):
                self._tries -= 1
                print(f"\n\tIncorrecto, el número de palabras es menor. Le quedan {self._tries} intentos.\n")
            else:
                self._tries -= 1
                print(f"\n\tIncorrecto, el número de palabras es mayor. Le quedan {self._tries} intentos.\n")

        # El bucle continuará mientras queden intentos y no esté solucionada la frase
        self.logger.debug("Iniciando fase 2 de juego.")
        while self._tries > 0 and not self.isAccomplished():
            print("\n\tLa frase tiene la siguiente forma: " + str(self._shadow))
            print(f"\tLe quedan {self._tries} intentos.")
            print("\n\tElija una de las siguientes opciones: ")
            print("\n\t1 - Adivinar letras\n\t2 - Adivinar palabras\n\t3 - Adivinar frase")

            try:
                opUser = int(input("\n\tOpción: "))

                if opUser < 1 or opUser > 3:
                    raise Exception

            except Exception as e:
                print("Valor insertado no válido, inserte un valor entre el 1 y el 3.")
                self.logger.error(f"Error: {str(e)}")
                continue

            avOpt = {1: self.adivLetras, 2: self.adivPalabras, 3: self.adivFrase}
            result = avOpt.get(opUser, 'Default controlado por excepciones')
            result()

        self.isWin(self.isAccomplished())

        self.logger.info("Fin juego.")

    # Adivinar letras
    def adivLetras(self):
        while True:
            letra = str(input("\n\tInserte letra: "))
            exist = self.charExists(letra)

            if exist == -1:
                # Control de errores
                self.logger.debug("Control de errores")
                print("\n\tValor insertado no válido, inserte otro.")
                continue
            elif exist:
                # El jugador ha acertado la letra
                self.logger.debug("El jugador ha acertado la letra")
                print(f"\n\tCorrecto, la frase contiene la letra insertada.\n\tForma actualizada.")
                break
            else:
                # El jugador no ha hacertado la letra
                self.logger.debug("El jugador no ha acertado la letra")
                self._tries -= 1
                self._lstIntentosLetras.append(letra)
                print(f"\tIncorrecto, la frase no contiene la letra insertada.\n\tLe quedan {self._tries} intentos.")
                break

    # Adivinar Palabras
    def adivPalabras(self):

        palabra = str(input("\n\tInserte palabra: "))
        exist = self.wordExists(palabra)

        if exist:
            # El jugador ha acertado la palabra
            self.logger.debug("El jugador ha acertado la palabra")
            print(f"\n\tCorrecto, la frase contiene la palabra insertada.\n\tForma actualizada.")
        else:
            # El jugador no ha hacertado la palabra
            self.logger.debug("El jugador no ha acertado la palabra")
            self._tries -= 1
            self._lstIntentosPalabras.append(palabra)
            print(f"\tIncorrecto, la frase no contiene la palabra insertada.\n\tLe quedan {self._tries} intentos.")

    # Adivinar Frase
    def adivFrase(self):

        frase = str(input("\n\tInserte la frase: "))
        exist = self.sentenceExists(frase)

        if exist:
            # El jugador ha acertado la frase
            self.logger.debug("El jugador ha acertado la frase")
            print(f"\n\tHa acertado la frase.\n\tForma actualizada.")
        else:
            # El jugador no ha hacertado la frase
            self.logger.debug("El jugador no ha acertado la frase")
            self._tries -= 1
            self._lstIntentosFrases.append(frase)
            print(f"\tIncorrecto, no ha acertado la frase.\n\tLe quedan {self._tries} intentos.")

    def isWin(self, value):
        if value:
            print("\n\tEnhorabuena, has ganado.")
            print("\tRegistrando victoria en el ranking ....")
            self.activeUser.updateSelfScore(1)
        else:
            print("No has ganado")

        print("\n\tMostrando intentos:")
        self.showTries()

    def showTries(self):
        print("\n\tIntentos de letras:")
        print("\n\t\t" + self.lstBonita(self._lstIntentosLetras))
        print("\n\tIntentos de palabras:")
        print("\n\t\t" + self.lstBonita(self._lstIntentosPalabras))
        print("\n\tIntentos de frases:")
        print("\n\t\t" + self.lstBonita(self._lstIntentosFrases))

    # -----------------------------------------------------------------------------------------------

    # Instrucciones

    def instr(self):
        self.logger.info("Mostramos las instrucciones del juego.")
        print("\n\tInstrucciones del juego")

        config = inOutFunctions.readConfig()

        self.logger.debug("Guardamos la info del json en un dataframe")
        df = pd.read_json(config['game_files']["game_instr_path"])

        self.logger.debug("Mostramos la info del dataframe")
        for x in df:
            print("\n\t" + x)  # Mostramos la categoría
            row = df[x].values.tolist()
            for y in row:
                # Si la línea no contiene un string, la saltamos
                if isinstance(y, float):
                    continue
                print("\t\t" + y)

        print("\n\tFin de instrucciones")
        self.logger.info("Instrucciones mostradas correctamente.")

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------

    # Método para mostrar los rankings

    def showRankings(self):
        self.logger.info("Mostrando Rankings")
        print(f"\nMostrando Rankings de {str(self.activeUser.name)}:")

        self.logger.debug("Guardamos la info del ranking en un dataframe")
        df = pd.read_csv(self.rankingFilePath, sep=",")

        self.logger.debug("Mostramos la info del usuario activo")
        userInfo = df[df["user"] == str(self.activeUser.name)]
        print(f"\n\tSu puntuación ha sido de: {userInfo['score'].values[0]}\n")

        self.logger.debug("Ordenamos la información")
        df = df.sort_values(by=['score'], ascending=False)
        self.logger.debug("Mostramos el resto de información")
        for x, y in df.values:
            print(f"\t{x} - {y}")

        self.logger.info("Fin mostrando Rankings")

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------

    # Método para ir al menú de usuario

    def changeUserMenu(self):

        while True:
            try:
                self.logger.info("Cambiamos de usuario")

                print("\nMENÚ - Cambiar de usuario")
                userOp = int(input("\n\t1 - Cambiar a usuario existente"
                                   "\n\t2 - Crear usuario nuevo"
                                   "\n\t0 - Volver"
                                   "\n\n\tOpción: "))

                # Control de errores
                if userOp < 0 or userOp > 2:
                    raise Exception

                # Alternativa a Switch
                avOpt = {1: self.chngUser, 2: self.createUser, 0: myBreak}
                result = avOpt.get(userOp, 'Default controlado por excepciones')

                result = result()
                if result or result == -1:
                    break

            except Exception as e:
                print("\n\tValor introducido no válido. Inserte un valor entre el 0 y el 2.")
                self.logger.error("Error inesperado: " + str(e))

    # Método para cambiar de usuario
    def chngUser(self):
        self.logger.info("Cambiando de usuario.")

        self.logger.debug("Leyendo csv y guardando información en un dataframe")
        df = pd.read_csv(self.usersFilePath, sep=",")

        self.logger.debug("Solicitando nombre del usuario ....")
        userName = str(input("\n\tInserte el nombre de usuario: "))

        self.logger.debug("Comprobando que el usuario insertado existe en el csv ....")
        exist = df[df["user"] == userName]

        if len(exist) > 0:
            self.logger.debug("El nombre de usuario existe, solicitando contraseña ....")

            userPasswd = str(input(f"\n\tContraseña del usuario {userName}: "))

            self.logger.debug("Sobreescribimos el dataframe con un nuevo dataframe que contiene "
                              "solo la fila del usuario")
            df = df[df["user"] == userName]
            dfPAsswd = df["passwd"].values[0]

            self.logger.debug("Comparamos las 2 contraseñas, y si coinciden, actualizamos el usuario activo")
            if generalFunctions.encript(userPasswd) == dfPAsswd:
                self.setActiveUser(userName, generalFunctions.encript(userPasswd))
                self.logger.info("Usuario activo actualizado.")

            return True
        else:
            self.logger.debug("El nombre de usuario NO existe. Avisamos al usuario.")
            print("\n\tNo existe nungún usuario con ese nombre.")

    # Método para crear usuario nuevo
    def createUser(self):
        self.logger.debug("Solicitamos la info del usuario a crear.")
        newName = str(input("\n\tInserte el nombre de usuario que quiere crear: "))

        while True:
            newPass = str(input("\n\tInserte la contraseña del nuevo usuario: "))

            if newPass == str(input("\tVuelva a escribir la contraseña: ")):
                break
            else:
                self.logger.debug("Las contraseñas no coinciden, volviendo a pedir.")
                print("\n\tLas contraseñas no coinciden. Repita el paso.")

        self.logger.info("\tCreando nuevo usuario.")
        print("\n\tCreando usuario nuevo ....")
        self.activeUser = User(newName, generalFunctions.encript(newPass))
        print("\tUsuario creado.")

        return True

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------

    # Método para salir del menú

    @dispatch()
    def exitMenu(self):
        self.logger.info("Saliendo de menú")
        print("\nSaliendo ....")
        self.logger.info("Fin Programa.")
        return exit(0)

    # -----------------------------------------------------------------------------------------------

    # Métodos relacionados con la gestión de usuarios

    # Busca el usuario con nombre insertado por params en el fichero usuarios.csv y si lo encuentra
    #   lo define como activo
    @dispatch(str, str)
    def setActiveUser(self, userName, passwd):
        self.logger.debug("Definimos el usuario activo.")
        # Leemos el fichero .csv
        dfUsers = pd.read_csv(self.usersFilePath, sep=",", dtype=object)

        # Guardamos el dataframe con la info de las filas que coinciden con el nombre y la contraseña
        res = dfUsers[dfUsers["passwd"] == str(passwd)]  # Filtramos por passwd
        res = res[res["user"] == str(userName).lower()]  # Filtramos por nombre

        # Comprobamos que el usuario con la contraseña introducidas existe
        if len(res) <= 0:
            self.logger.debug(f"No existe el usuario {userName} con la contraseña indicada en el fichero csv. "
                              f"Retornamos False.")
            return False

        self.logger.debug(f"Existe el usuario {userName} en el fichero csv. Lo marcamos como activo y retornamos True.")
        self.activeUser = User(userName, passwd)
        return True

    # -----------------------------------------------------------------------------------------------

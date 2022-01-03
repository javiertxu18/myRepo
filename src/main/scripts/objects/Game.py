from multipledispatch import dispatch
from src.main.scripts.functions import inOutFunctions, generalFunctions
from src.main.scripts.objects.Objective import Objective
from src.main.scripts.objects.User import User
import pandas as pd


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

        print(f"Beinvenido/a  {self.activeUser.name}")

        while True:
            print("MENÚ - Adivina la frase")
            print("1 - Jugar")
            print("2 - Ver ranking")
            print("0 - Salir")

            # Comprobamos que el usuario ha insertado un valor válido
            try:
                userOption = int(input("Opción: "))

                if userOption < 0 or userOption > 2:
                    raise ValueError("Valor fuera de límites. Introduzca un valor numérico entre el 0 y el 2.")

            except ValueError as ve:
                print("\nValor no válido. Introduzca un valor numérico entre el 0 y el 2.\n")
                self.logger.error(str(ve))
                continue
            except Exception as e:
                print("\nError, valor introducido no válido. Introduzca un valor numérico entre el 0 y el 2.\n")
                self.logger.error(str(e))
                continue

            # Alternativa a Switch
            avOpt = {1: self.playGame, 2: self.showRankings, 0: self.exitMenu}
            result = avOpt.get(userOption, 'Default controlado por excepciones')
            result()

    # -----------------------------------------------------------------------------------------------

    # Métodos para jugar al juego

    def playGame(self):
        self.logger.info("Jugando juego")
        print("jugar")
        self.logger.info("Fin jugando juego")

    # Fase1:

    # -----------------------------------------------------------------------------------------------

    # Método para mostrar los rankings

    def showRankings(self):
        self.logger.info("Mostrando Rankings")
        print("Mostrando Rankings")
        self.logger.info("Fin mostrando Rankings")

    # -----------------------------------------------------------------------------------------------

    # Método para salir del menú

    def exitMenu(self):
        self.logger.info("Saliendo de menú")
        print("salir")

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
        res = dfUsers[dfUsers["passwd"] == str(passwd).lower()]  # Filtramos por passwd
        res = res[res["user_name"] == str(userName).lower()]  # Filtramos por nombre

        # Comprobamos que el usuario con la contraseña introducidas existe
        if len(res) <= 0:
            self.logger.debug(f"No existe el usuario {userName} con la contraseña indicada en el fichero csv. "
                              f"Retornamos False.")
            return False

        self.logger.debug(f"Existe el usuario {userName} en el fichero csv. Lo marcamos como activo y retornamos True.")
        self.activeUser = User(userName, passwd)
        return True

    # -----------------------------------------------------------------------------------------------

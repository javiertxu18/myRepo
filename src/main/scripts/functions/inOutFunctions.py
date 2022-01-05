import configparser
import sys
import inspect
from src.main.scripts.functions import generalFunctions


# -----------------------------------------------------------------------------------------------
# DESC:
#   Configura el config parser (Para leer y escribir en el fichero config.ini)
#   Configuramos el logger
# Params:
#   No tiene
# Return:
#   Nada
# Llamar a esta función solo desde el main.py
def setConfig(logger_level=30):
    # Preparamos el logger
    generalFunctions.setLogger()

    # Preparamos el configParser
    try:
        # Control para que se llame a la función únicamente desde main.py
        if inspect.stack()[1][1].split("/")[-1] != "main.py":
            raise "You can only call this method from main.py"

        # Preparamos el configParser
        conf = configparser.ConfigParser()
        # Leemos el fichero config.ini
        conf.read(sys.path[1] + "/config.ini")
        # Escribimos en el configParser (No en el fichero)
        conf['DEFAULT']['root_path'] = sys.path[1]
        conf['DEFAULT']['config_path'] = conf['DEFAULT']['root_path'] + "/config.ini"
        conf['DEFAULT']['logger_level'] = str(logger_level)  # Nivel del logger por defecto

        # Creamos una key nueva para guardar datos sobre los ficheros
        conf['game_files'] = {}
        conf['game_files']["ranking_path"] = conf['DEFAULT']['root_path'] + "/src/main/resources/ranking.csv"
        conf['game_files']["users_path"] = conf['DEFAULT']['root_path'] + "/src/main/resources/users.csv"
        conf['game_files']["game_instr_path"] = conf['DEFAULT']['root_path'] + "/src/main/resources/game_instr.json"

        # Sobreescribimos el fichero y guardamos la info nueva
        with open(conf['DEFAULT']['config_path'], 'w') as configfile:
            conf.write(configfile)
    except Exception as e:
        # Este error lo mostramos por pantalla ya que el logger no está configurado.
        print("Error en setConfig(): " + str(e))
        pass


# -----------------------------------------------------------------------------------------------
# DESC:
#   Devuelve el configParser para que se pueda leer el fichero config.ini cómodamente
# Params:
#   No tiene
# Return:
#   configParser si ha ido bien, False si ha ido mal


def readConfig():
    try:
        # Preparamos el configParser
        conf = configparser.ConfigParser()
        # Leemos el fichero config.ini
        conf.read(sys.path[1] + "/config.ini")
        # Retornamos el configParser
        return conf
    except Exception as e:
        logger = generalFunctions.getLogger("inOutFunctions")
        logger.error(str(e))
        return False

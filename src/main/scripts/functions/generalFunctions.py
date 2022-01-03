import hashlib
import logging
import sys
from multipledispatch import dispatch

# -----------------------------------------------------------------------------------------------

# DESC: Encripta el string pasado por parámetro
# Params:
#   str: El string que queremos encriptar
# Return: El string encriptado.
from src.main.scripts.functions import inOutFunctions


@dispatch(str)
def encript(string):
    return hashlib.md5(str(string).encode()).hexdigest()


# -----------------------------------------------------------------------------------------------

# DESC: Prepara el logger
# Params:
#   No tiene
# Return:
#   True si se ha creado, False si no se ha creado
@dispatch()
def setLogger():
    try:
        logging.basicConfig(
            filename=sys.path[1] + "/.log",  # Fichero donde vamos a guardar la info
            filemode="a",  # Modo en el que vamos a guardar la info (append)
            format='%(asctime)s %(levelname)s(%(name)s) '
                   '%(filename)s:line(%(lineno)s) '
                   '-> %(message)s',  # Formato de la info
            level=logging.INFO,  # Level por defecto
            datefmt='%Y-%m-%d %H:%M:%S')  # Formato de fecha
        return True
    except Exception as e:
        print("Error configurando el logger: " + str(e))
        return False


# Params:
#   str: El nombre del logger que se crea
# Return:
#   El logger
@dispatch(str)
def setLogger(name):
    try:
        if setLogger():
            return getLogger(name)
        return False
    except Exception as e:
        print("Error configurando el logger: " + str(e))
        return False


# -----------------------------------------------------------------------------------------------

# DESC:
#   Devuelve el logger.
#   Si el config.ini está configurado, el nivel del logger se coje de ahí. Sino se pone en INFO por defecto.
# PARAMS:
#   name: Nombre del logger
# Return
#   el logger
@dispatch(str)
def getLogger(name):
    # Preparamos el nivel del logger
    #   Si está en el config.ini se coje de ahí, sino se pone el nivel por defecto
    try:
        config = inOutFunctions.readConfig()
        level = int(config["DEFAULT"]["logger_level"])
    except:
        level = logging.ERROR

    # Preparamos el logger
    logger = logging.getLogger(str(name))
    logger.setLevel(level)
    setLogger()

    # Añadimos un Handler al logger para que muestre por consola los mensajes
    console = logging.StreamHandler()
    console.setLevel(level)

    # Preparamos el formato del Handler y lo añadimos
    format = logging.Formatter('%(asctime)s %(levelname)s(%(name)s) '
                               '%(filename)s:line(%(lineno)s) '
                               '-> %(message)s')
    console.setFormatter(format)

    # Añadimos el handler al logger y lo retornamos
    logger.addHandler(console)

    return logger

# -----------------------------------------------------------------------------------------------

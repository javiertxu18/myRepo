from src.main.scripts.functions import generalFunctions, inOutFunctions
import pandas as pd


class User:

    # Constructor
    def __init__(self, name, passwd, score=0):
        self.logger = generalFunctions.getLogger("User")  # Logger
        self.name = name  # Nombre del usuario
        self.passwd = passwd  # Contraseña del usuario
        self.score = score  # Puncuación del usuario
        self.rankingFilePath = inOutFunctions.readConfig()["game_files"]["ranking_path"]  # Ruta al fichero de rankings
        self.logger.debug("Creamos el usuario " + str(self.name))   # Mensaje para el logger

        self.updateSelfScore()  # Actualizamos el score con el fichero de rankings

    # Métodos

    # -----------------------------------------------------------------------------------------------

    # DESC: Actualiza el self.score. Si no se ha registrado nunca en rankings.csv, crea uno nuevo, y si ya existe, lo
    #   actualiza.
    # Params:
    #   addScore: Cantidad de escore que se añade o se resta de la score.
    # Return:
    #   True: Si _todo ha ido bien
    #   False: Si ha habido algún error.
    def updateSelfScore(self, addScore=0):
        # Leemos el fichero de scores buscando el nombre de usuario
        dfScoreFile = pd.read_csv(self.rankingFilePath, sep=",")
        # Buscamos el usuario en el dataFrame
        dfUserScore = dfScoreFile[dfScoreFile["user"] == str(self.name).lower()]
        # Comprobamos si está vacío el df
        if (len(dfUserScore) == 0):
            self.logger.debug("Creamos el score del usuario " + str(self.name))
            newScore = 0 + addScore

            # Si el newScore < 0, hacemos que el score sea 0, para que no haya scores negativas
            if newScore < 0:
                newScore = 0

            dfScoreFile = dfScoreFile.append({'user': self.name, 'score': newScore}, ignore_index=True)
        else:
            self.logger.debug("Actualizamos el score del usuario " + str(self.name))
            newScore = dfUserScore[dfUserScore["user"] == "guest"].values[0][1] + addScore

            # Si el newScore < 0, hacemos que el score sea 0, para que no haya scores negativas
            if newScore < 0:
                newScore = 0

            dfScoreFile.loc[dfScoreFile['user'] == "guest", 'score'] = newScore

        # Actualizamos el score en el objeto
        self.score = newScore

        # Guardamos el dataframe en el csv con los cambios realizados
        dfScoreFile.to_csv(self.rankingFilePath, sep=",", index=False)
        # Retornamos True
        return True
    # -----------------------------------------------------------------------------------------------

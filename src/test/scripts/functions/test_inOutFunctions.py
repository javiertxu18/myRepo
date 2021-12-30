import configparser
from src.main.scripts.functions.inOutFunctions import readConfig

def test_readConfig():
    assert readConfig() == configparser.ConfigParser()
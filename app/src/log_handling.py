from configure import *


def log_regstra_movimentos(tabuleiro):
    with open(LOG_FILE_PATH,'a') as arquivo:
        arquivo.write( str(tabuleiro))

def log_recupera_movimentos():
    with open(LOG_FILE_PATH,'r') as arquivo:
        arquivo.read()
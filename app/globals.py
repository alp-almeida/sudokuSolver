from tkinter.constants import FALSE
import testing as tb                                # possui os dados do tabuleiro utilizado.
from copy import deepcopy

# Definição do tabuleiro
teste = FALSE
if (teste):
    tabuleiro = deepcopy(tb.GABARITO)
else:
    tabuleiro = deepcopy(tb.TABULEIRO_ORIGINAL)



# Variaveis de jogada
jPosicao = ''
jEntrada = ''
bool_jogar = False



mapa_botoes = []
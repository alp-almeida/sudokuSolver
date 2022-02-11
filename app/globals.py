
import testing as tb                                # possui os dados do tabuleiro utilizado.
from copy import deepcopy

# Definição do tabuleiro
teste = False
if (teste):
    tabuleiro = deepcopy(tb.GABARITO)
else:
    tabuleiro = deepcopy(tb.TABULEIRO_ORIGINAL)


# Variaveis de jogada
jPosicao = ''
jEntrada = ''
bool_jogar = False



mapa_botoes = []

def gerar_mapa_possiveis_entradas():
    '''
    Vai gerar o mapa de acordo com o tabuleiro atual.
    '''
    mapa = [[],[],[],[],[],[],[],[],[]] 
    for k in range(9):
        for i in range(9):
            for j in range(9):
                mapa[k].append([i,j])
    
    
    for nlinha, linha in enumerate(tabuleiro):
        for ncoluna, valor in enumerate(linha):
            if valor != 0:
                'tem que tirar todas as ocorrencias daquelas coordenadas'
                for index, map_line in enumerate(mapa):
                    
                    if [nlinha,ncoluna] in map_line:
                        mapa[index].remove([nlinha,ncoluna])
                        
                
    
    return mapa

# pos 0 = 1 pos 8 = 9
mapa_possiveis_entradas  = gerar_mapa_possiveis_entradas()

def ler_mapa():
    print('---')
    for index,line in enumerate(mapa_possiveis_entradas):
        print(index,len(line),sep=" -> ")


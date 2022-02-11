from numpy import transpose
from configure import ENTRADA_OP
from globals import *
from sudoku_back_app import acesso_quadrantes,mapear_quadrados_tabuleiro




def percorrer_tabuleiro():
    '''
    Percorre todo o tabuleiro e para cada celular vazia irá avaliar as possiveis jogadas
    \tcaso sobre apenas 1 opção ela será vinculada à celula em questão.
    '''
    for index,campo in enumerate(mapa_botoes):
        texto = campo['text']
        linha = int(index/9)
        coluna = int((index/9 - int(index/9))*9)
        #print(index,linha,coluna,texto,sep="\t")
        if (texto == ''):
            jogadas_possíveis = verificar_possiveis_jogadas(linha,coluna)
            for entrada in jogadas_possíveis:
                analise_por_opcoes(entrada)
    
    ler_mapa()
    
    '''

    '''


    return 0

def verificar_possiveis_jogadas(linha,coluna):
    """
    Retorna um vetor com as entradas validas para aquele campo.\n
    \nSteps |------------------------------------------------------------------------
    dada uma determinada celula\n
    \titera a linha e suas celulas\n
    \titera a coluna e suas celulas\n
    \titera o quadrante e suas celulas\n
    \tarmazena os dados das iterações e elimina todas do vetor de possibilidades\n
    
    """
    #iterando a linha
    tLinha = tabuleiro[linha]
    posLinha = []
    for item in tLinha:
        if item != 0 :
            posLinha.append(item)
    #print(posLinha)
    
    tColuna = transpose(tabuleiro)[coluna]
    posColuna = []
    for item in tColuna:
        if item != 0:
            posColuna.append(item)
    #print(posColuna)
    
    num_quadrante = acesso_quadrantes(f'{linha},{coluna}') # inteiro
    list_quadrantes = mapear_quadrados_tabuleiro(tabuleiro) # vetor
    quadrante = list_quadrantes[num_quadrante] #vetor
    posQuad = []
    for item in quadrante:
        if item != 0:
            posQuad.append(item)

    entradas_registradas = list(set(posLinha + posColuna + posQuad))
    entradas = deepcopy(ENTRADA_OP)
    entradas.remove(0)

    for item in entradas_registradas:
        entradas.remove(item)
    print([linha,coluna],entradas,sep="\t ")
    '''
    [2, 3, 4, 5, 9]
    [1,6,7,8]
    '''
    #retorno do compilado
    return entradas

def analise_por_opcoes(entrada):
    """
    Retorna um vetor com os campos que podem receber aquele determinado número.
    \n
    Selecionar a entrada a ser avaliadade vinda da função verificar_possiveis_jogadas().
    Varrer todo o tabuleiro olhando todos os campos marcados com aquele valor
    Para cada campo encontrado com o valor serão coletados e eliminados das possibilidades de receber aquele valor.\n
    \tlinha, \n
    \tcoluna \n
    \tquadrante 
    """
    vec = list()
    for index,campo in enumerate(mapa_botoes):
        texto = campo['text']
        coluna = int(index/9)
        linha = int((index/9 - int(index/9))*9)

        if texto == entrada:
            #existente = [linha,coluna]
            remover_possibilidades_na_linha(linha)
            ler_mapa()

    
    #print(f'{entrada} -> {vec}', sep='')


def remover_possibilidades_na_linha(linha):
    for coluna in range(9):
        #vai de 0 a 8
        if [linha,coluna] in mapa_possiveis_entradas:
            mapa_possiveis_entradas[linha].remove([linha,coluna])
    return 0

def remover_possibilidades_na_coluna():

    return 0

import GUI_app
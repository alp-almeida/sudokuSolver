from copy import deepcopy
from numpy import string_
from configure import *
from numpy import transpose




def criar_campo():
    campo = 0
    return campo

def criar_linha(nCampos=9):
    linha = [criar_campo()] * nCampos
    return linha

def criar_tabuleiro(nLinhas=9):
    tabuleiro_CT = []
    for i in range(0, nLinhas):
        tabuleiro_CT.append(criar_linha(nLinhas))
        # print tabuleiro_CT
    return tabuleiro_CT

def mostrar_tabuleiro(tabuleiro_MT):
    for lin in tabuleiro_MT:
        print(lin)

def acesso_quadrantes(strCoord):
    quad = {
        '0,0': 0, '0,1': 0, '0,2': 0,          '0,3': 1, '0,4': 1, '0,5': 1,         '0,6': 2, '0,7': 2, '0,8': 2,
        '1,0': 0, '1,1': 0, '1,2': 0,          '1,3': 1, '1,4': 1, '1,5': 1,         '1,6': 2, '1,7': 2, '1,8': 2,
        '2,0': 0, '2,1': 0, '2,2': 0,          '2,3': 1, '2,4': 1, '2,5': 1,         '2,6': 2, '2,7': 2, '2,8': 2,
        
        '3,0': 3, '3,1': 3, '3,2': 3,          '3,3': 4, '3,4': 4, '3,5': 4,         '3,6': 5, '3,7': 5, '3,8': 5,
        '4,0': 3, '4,1': 3, '4,2': 3,          '4,3': 4, '4,4': 4, '4,5': 4,         '4,6': 5, '4,7': 5, '4,8': 5,
        '5,0': 3, '5,1': 3, '5,2': 3,          '5,3': 4, '5,4': 4, '5,5': 4,         '5,6': 5, '5,7': 5, '5,8': 5,

        '6,0': 6, '6,1': 6, '6,2': 6,          '6,3': 7, '6,4': 7, '6,5': 7,         '6,6': 8, '6,7': 8, '6,8': 8,
        '7,0': 6, '7,1': 6, '7,2': 6,          '7,3': 7, '7,4': 7, '7,5': 7,         '7,6': 8, '7,7': 8, '7,8': 8,
        '8,0': 6, '8,1': 6, '8,2': 6,          '8,3': 7, '8,4': 7, '8,5': 7,         '8,6': 8, '8,7': 8, '8,8': 8,
    }
    return quad[strCoord]

def mapear_quadrados_tabuleiro(t):
    linha = 0
    coluna = 0
    q11 = t[linha][coluna:coluna+3]
    q11 += (a for a in t[linha+1][coluna:coluna+3])
    q11 += (a for a in t[linha+2][coluna:coluna+3])

    coluna = 3
    q12 = t[linha][coluna:coluna+3]
    q12 += (a for a in t[linha+1][coluna:coluna+3])
    q12 += (a for a in t[linha+2][coluna:coluna+3])

    coluna = 6
    q13 = t[linha][coluna:coluna+3]
    q13 += (a for a in t[linha+1][coluna:coluna+3])
    q13 += (a for a in t[linha+2][coluna:coluna+3])

    linha = 3
    coluna = 3
    q21 = t[linha][coluna:coluna+3]
    q21 += (a for a in t[linha+1][coluna:coluna+3])
    q21 += (a for a in t[linha+2][coluna:coluna+3])

    coluna = 3
    q22 = t[linha][coluna:coluna+3]
    q22 += (a for a in t[linha+1][coluna:coluna+3])
    q22 += (a for a in t[linha+2][coluna:coluna+3])

    coluna = 6
    q23 = t[linha][coluna:coluna+3]
    q23 += (a for a in t[linha+1][coluna:coluna+3])
    q23 += (a for a in t[linha+2][coluna:coluna+3])

    linha = 6
    coluna = 6
    q31 = t[linha][coluna:coluna+3]
    q31 += (a for a in t[linha+1][coluna:coluna+3])
    q31 += (a for a in t[linha+2][coluna:coluna+3])

    coluna = 3
    q32 = t[linha][coluna:coluna+3]
    q32 += (a for a in t[linha+1][coluna:coluna+3])
    q32 += (a for a in t[linha+2][coluna:coluna+3])

    coluna = 6
    q33 = t[linha][coluna:coluna+3]
    q33 += (a for a in t[linha+1][coluna:coluna+3])
    q33 += (a for a in t[linha+2][coluna:coluna+3])

    return [q11, q12, q13, q21, q22, q23, q31, q32, q33]

def entrada_tabuleiro(numeros, tabuleiro_INP):
    linha = 0
    coluna = 0
    for numero in numeros:
        tabuleiro_INP[linha][coluna] = numero
        coluna += 1
        if (coluna == 9):
            coluna = 0
            linha += 1

    return tabuleiro_INP

def limites(LINHA,COLUNA,VALOR):
    ckLINHA  = MIN_LINHAS_COLUNAS <= LINHA  <= MAX_LINHAS_COLUNAS
    ckCOLUNA = MIN_LINHAS_COLUNAS <= COLUNA <= MAX_LINHAS_COLUNAS
    #ckVALOR  = ENTRADA_MIN        <= VALOR  <= ENTRADA_MAX #and VALOR != ENTRADA_NULA
    ckVALOR = VALOR in ENTRADA_OP

    return ckLINHA and ckCOLUNA and ckVALOR

def validar_entrada(entrada):
    entrada_split = entrada.split(',',3)
    LINHA  = int (entrada_split[0]) 
    COLUNA = int (entrada_split[1] *1)
    VALOR  = int (entrada_split[2] *1)

    tamanho = len(entrada_split)
    bool_tamanho = tamanho == 3
    bool_limites = limites( LINHA,COLUNA,VALOR )
    bool_go = bool_tamanho and bool_limites
    #print (bool_tamanho,bool_limites,bool_go)
    if (bool_go):
        return [LINHA,COLUNA,VALOR]
    else:
        return ''

def registrar_jogada(LINHA,COLUNA,VALOR,tabuleiro):
    tabuleiro[LINHA][COLUNA] = VALOR

def entrada_duplicada_linha(valor,linha_num,tabuleiro):
    b_dup_linha = False
    nOcorrencias = 0
    for coluna in tabuleiro[linha_num]:
        if valor == coluna:
            nOcorrencias +=1
        b_dup_linha = (int(nOcorrencias) >= 2)
        
    return b_dup_linha

def entrada_duplicada_coluna(valor,coluna_num,tabuleiro):
    return entrada_duplicada_linha(valor,coluna_num,transpose(tabuleiro))

def entrada_duplicada_quadrado(valor,linha_num,coluna_num,tabuleiro):
    qNum = acesso_quadrantes(f'{linha_num},{coluna_num}') # inteiro
    qList = mapear_quadrados_tabuleiro(tabuleiro) # vetor
    quad = qList[qNum] #vetor
    b_quad = False
    nOcorrencias = 0
    for q in quad:
        if q == valor:
            nOcorrencias += 1 
        b_quad = (nOcorrencias >= 2)
    return b_quad
    
def checar_duplicidades(valor,linha_num,coluna_num,tabuleiro):
    bLinha      = entrada_duplicada_linha(valor,linha_num,tabuleiro)
    bColuna     = entrada_duplicada_coluna(valor,coluna_num,tabuleiro)
    bQuadrante  = entrada_duplicada_quadrado(valor,linha_num,coluna_num,tabuleiro)
    bFinal = (bLinha or bColuna or bQuadrante)
    return bFinal

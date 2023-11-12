from copy import deepcopy
from configure import *





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

#print('0,0,1')
#print(':=',validar_entrada ('0,0,1'))

def registrar_jogada(LINHA,COLUNA,VALOR,tabuleiro):
    tabuleiro[LINHA][COLUNA] = VALOR

def log_registra_movimentos(tabuleiro):
    with open(LOG_FILE_PATH,'a') as arquivo:
        arquivo.write( str(tabuleiro))

def log_recupera_movimentos():
    with open(LOG_FILE_PATH,'r') as arquivo:
        arquivo.read()
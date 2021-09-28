from copy import deepcopy

def criar_campo():
    campo = 0
    return campo

def criar_linha(nCampos = 9):
    linha = [criar_campo()] * nCampos
    return linha
    
def criar_tabuleiro(nLinhas = 9):
    tabuleiro_CT = []
    for i in range(0,nLinhas):
        tabuleiro_CT.append(criar_linha(nLinhas))
        #print tabuleiro_CT
    return tabuleiro_CT
    
def mostrar_tabuleiro(tabuleiro_MT):
    for lin in tabuleiro_MT:
        print lin

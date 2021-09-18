from copy import deepcopy

def criar_campo():
    campo = 0
    return campo

def criar_linha():
    linha = [criar_campo()]*9
    return linha
    
def criar_tabuleiro():
    tabuleiro_CT = []
    for i in range(0,9):
        tabuleiro_CT.append(criar_linha())
        #print tabuleiro_CT
    return tabuleiro_CT
    
def mostrar_tabuleiro(tabuleiro_MT):
    for lin in tabuleiro_MT:
        print lin

from sudoku_back_app import *
from configure import *
from numpy import transpose

def regra_da_vitoria(tabuleiro_RDV):

    bool_linhas    = vitoria_soma_linha(tabuleiro_RDV)
    bool_colunas   = vitoria_soma_colunas(tabuleiro_RDV)
    bool_quadrados = vitoria_soma_quadrados(tabuleiro_RDV)
    bool_total     = vitoria_soma_tabuleiro(tabuleiro_RDV)    
    bool_vitoria   = (bool_linhas and bool_colunas) and (bool_total and bool_quadrados)
    #print(bool_linhas,bool_colunas,bool_quadrados,bool_total,"Vitoria := " ,bool_vitoria)

    return bool_vitoria


def vitoria_soma_linha(tabuleiro_VSL):
    bool_VSL = True
    for lin in tabuleiro_VSL:
        if vitoria_soma_linha_checa_linha(lin) != SOMA_LINHAS_COLUNAS:
            bool_VSL = False
    return bool_VSL

def vitoria_soma_linha_checa_linha(linha):
	return sum(linha)

def vitoria_soma_colunas(tabuleiro_VSC):
	return vitoria_soma_linha(transpose(tabuleiro_VSC))

def vitoria_soma_tabuleiro(tabuleiro_VST):
    VST = 0
    for lin in tabuleiro_VST:
        VST += sum(lin)
    bool_VST = (VST == SOMA_TABULEIRO)
    return bool_VST

def vitoria_soma_quadrados(t):
	mapa_quadrados = mapear_quadrados_tabuleiro(t)

	for quadro in mapa_quadrados:
		if (sum(quadro) != SOMA_QUADRADOS):
			return False
			break
	
	return True
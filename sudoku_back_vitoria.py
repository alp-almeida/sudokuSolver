import sudoku_back_app
import numpy as np

def vitoria_soma_linha_checa_linha(linha):
	print 'Linha ${} tem valor ${}'.format(linha,,sum(linha))
	return sum(linha)

def vitoria_soma_linha(tabuleiro_VSL):
    bool_VSL = True
    for lin in tabuleiro_VSL:
        if vitoria_soma_linha_checa_linha(lin) != 45:
            bool_VSL = False
    return bool_VSL

def vitoria_soma_colunas(tabuleiro_VSC):
	return vitoria_soma_linha(np.transpose(tabuleiro_VSC))

def vitoria_soma_tabuleiro(tabuleiro_VST):
    VST = 0
    for lin in tabuleiro_VST:
        VST += sum(lin)
    bool_VST = (VST == 405)
    return bool_VST

def regra_da_vitoria(tabuleiro_RDV):
    #somaLinhas = 45
    soma_linhas = vitoria_soma_linha(tabuleiro_RDV)
    
    #somaColunas = 45
    soma_colunas = vitoria_soma_colunas(tabuleiro_RDV)
    
    #somaQuadradoMenor = 45
    
    #somaTotal = 405
    soma_total = vitoria_soma_tabuleiro(tabuleiro_RDV)


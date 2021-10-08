import sudoku_back_app

import numpy as np

def vitoria_soma_linha_checa_linha(linha):
	#print 'Linha {0} tem valor {1}'.format(linha,sum(linha))
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

def vitoria_soma_quadrados(t, vQuadrado = False , hQuadrado = False):
	linha = 0
	r11 = [t[linha][0:3] , t[linha+1][0:3] , t[linha+2][0:3]]
	q11 = []
	for lineOf3 in r11:
		for i in lineOf3: 
			q11.append( i ) 
	
	q12 = [t[linha][3:6] , t[linha+1][3:6] , t[linha+2][3:6]]
	q13 = [t[linha][6:9] , t[linha+1][6:9] , t[linha+2][6:9]]
	linha = 3
	q21 = [t[linha][0:3] , t[linha+1][0:3] , t[linha+2][0:3]]
	q22 = [t[linha][3:6] , t[linha+1][3:6] , t[linha+2][3:6]]
	q23 = [t[linha][6:9] , t[linha+1][6:9] , t[linha+2][6:9]]
	linha = 6
	q31 = [t[linha][0:3] , t[linha+1][0:3] , t[linha+2][0:3]]
	q32 = [t[linha][6:9] , t[linha+1][6:9] , t[linha+2][6:9]]
	q33 = [t[linha][6:9] , t[linha+1][6:9] , t[linha+2][6:9]]
	print (q11)
	print (sum(q11))
	if (not vQuadrado and not hQuadrado):
		#Continuar a criar a regra para a soma
		#contrauir uma regra para olha cada quadro separadamente
		False
	
	
	
	
	
def regra_da_vitoria(tabuleiro_RDV):
    #somaLinhas = 45
    soma_linhas = vitoria_soma_linha(tabuleiro_RDV)
    
    #somaColunas = 45
    soma_colunas = vitoria_soma_colunas(tabuleiro_RDV)
    
    #somaQuadradoMenor = 45
    #soma_quadrados = vitoria_soma_quadrados(tabuleiro)
    
    #somaTotal = 405
    soma_total = vitoria_soma_tabuleiro(tabuleiro_RDV)
    
    bool_vitoria = (soma_linhas and soma_colunas) and soma_total
    #print 'Linhas {0} Colunas {1} Total {2}'.format(soma_linhas,soma_colunas,soma_total)






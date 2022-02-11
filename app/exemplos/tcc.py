# -*- coding: utf-8 -*-
# https://www.tutorialspoint.com/execute_python3_online.php
import time
from tcc_mapa import *
from tcc_dicionario import *

print(">>>   Starting process: \n")

 
def clonaLista(lista):
	clone = []
	for c in lista:
		clone.append(c[:])
	return clone
 
def menor_rota(origem,destino,matriz):
	global distancia_menor_rota
	global dist_temp_rota
	global caminho_melhor_rota
    
	caminho_temp_rota.append(dict[origem])
    
	while(sum(matriz[origem]) > 0 ):
		peso_proximo_no = min(numero for numero in matriz[origem] if numero != 0)
		proximo_no = matriz[origem].index(peso_proximo_no)
		matriz[proximo_no][origem]=0
		matriz[origem][proximo_no]=0

		if(dist_temp_rota + peso_proximo_no > distancia_menor_rota):
			continue

		dist_temp_rota += peso_proximo_no
		if( proximo_no == destino ):
			if(dist_temp_rota < distancia_menor_rota):
				caminho_temp_rota.append(dict[proximo_no])
				caminho_melhor_rota = caminho_temp_rota[:]
				distancia_menor_rota = dist_temp_rota
				caminho_temp_rota.pop()
				menor_rota(proximo_no,destino,clonaLista(matriz))
				dist_temp_rota -= peso_proximo_no
				caminho_temp_rota.pop()

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

#-------------------| Variável Global |-------------------------

caminho_temp_rota = []
dist_temp_rota = 0
distancia_menor_rota = 1000000
caminho_melhor_rota = []
#-------------------|InicioProcessamento|----------------------

origem = 23
destino = 7
if (origem in dict and destino in dict):
	print("\t\tSearching for a better route ...")
	menor_rota(origem,destino,clonaLista(AD))

	#Mostrando os Resultados
	print('Melhor rota :')
	for cidade in caminho_melhor_rota: print('\t',cidade)
	
	print( f'Distância {round(distancia_menor_rota,2)} kms')
	


print('>>>   Ending process ...')






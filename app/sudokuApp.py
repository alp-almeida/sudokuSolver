
from numpy import equal
from testing import *
from sudoku_back_app import *
from sudoku_back_vitoria import *
from configure import *
from strings import *

def mensagem_de_vitoria():
        print (STR_MENSAGEM_VITORIA)

def main():
    CLS()
    #tabuleiro = criar_tabuleiro()   
    tabuleiro = TABULEIRO_ORIGINAL
    
    while (True):
        #log_registra_movimentos(tabuleiro)
        mostrar_tabuleiro(tabuleiro)
        
        LINHA,COLUNA,VALOR = validar_entrada(input(STR_SOLICITACAO_DE_JOGADA))
        registrar_jogada(LINHA,COLUNA,VALOR,tabuleiro)

        if (regra_da_vitoria(tabuleiro)):
            mensagem_de_vitoria()
            break
        CLS()


    #b.mostrar_tabuleiro(tabuleiro)
    
    
    

    


# aqui executa o aplicativo
main()

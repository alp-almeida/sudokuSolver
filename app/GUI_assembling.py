import ctypes
import tkinter as tk
from globals import *
from GUI_config import *
from GUI_themes import *
from strings import STR_MENSAGEM_VITORIA
from sudoku_back_app import *
from sudoku_back_vitoria import regra_da_vitoria

def atualiza_valor_celula(LINHA,COLUNA,VALOR):
    item = mapa_botoes[LINHA*9 + COLUNA]
    item['text'] = VALOR

def pega_posicao_botao(text_var,local, local_name):
    
    global tabuleiro
    
    if( local_name == FRAME_TAB ):
        global jPosicao
        jPosicao = text_var
    
    elif(local_name == FRAME_ENTRADAS and jPosicao != ''):
        global jEntrada 
        global bool_jogar

        jEntrada = text_var
        bool_jogar = True
    
    jogadaStr = "{0},{1}".format(jPosicao,jEntrada)
    
    if (bool_jogar):
        bool_jogar = not bool_jogar
        LINHA,COLUNA,VALOR = validar_entrada(jogadaStr)
        
        registrar_jogada(LINHA,COLUNA,VALOR,tabuleiro)
        atualiza_valor_celula(LINHA,COLUNA,VALOR)
        pintar_tabuleiro()
        pintar_duplicidades(tabuleiro)
        
        jPosicao = ''
        jEntrada = ''
        b_vitoria = regra_da_vitoria(tabuleiro)
        
        if (b_vitoria):
            #mensagem_de_vitoria()
            title = "Vitoria"
            text = STR_MENSAGEM_VITORIA
            ctypes.windll.user32.MessageBoxW(0, text, title, 0)


def criar_botao(local,text_var,linha,coluna , local_name):
    btn_state = tk.NORMAL
    #btn_font = "-weight normal -size 16"
    btn_font = "-family helvetica -size 12"

    if( local_name == FRAME_TAB ):
        #saidaStr = "{0},{1}".format(linha,coluna)
        saidaStr = f'{linha},{coluna}'
        
        if int(text_var) != 0 :
            btn_state = tk.DISABLED
            #btn_font = "-weight bold -size 16"
            btn_font = "-family helvetica -size 12"
        else:
            text_var = ''
    else:
        saidaStr = "{0}".format(text_var)
    
    btn = tk.Button(local)
    btn.configure( text    = text_var )
    btn.configure( width   = CELL_WIDTH )
    btn.configure( height  = CELL_HEIGHT )
    btn.configure( command = lambda: pega_posicao_botao(saidaStr,local,local_name=local_name) )
    btn.configure( pady    = 1 , padx  = 1)
    btn.configure( state   = btn_state)
    btn.configure( font    = btn_font)
    
    return btn


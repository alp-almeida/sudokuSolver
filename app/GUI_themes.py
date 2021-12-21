from globals import *
from sudoku_back_app import checar_duplicidades

''' bg , q1 , q2 , q3'''
# BG COLOR
color_black         = "#000000"
color_grey_deep     = "#222831"
color_grey_medium   = "#393E46"

#USADO PARA FONTES EM DARK THEMES
color_white_smoke  = "#F5F5F5"

# PINK THEME
def tema_rosa():
    bg       = color_black
    c1     = "#86003C"
    c2   = "#E41F7B"
    dup    = "#FF8BA0"
    fg = color_white_smoke
    return bg,c1,c2,dup,fg

# RED THEME
def tema_vermelho():
    bg        = color_black
    c1      = "#3D0000"
    c2    = "#950101"
    dup     = "#FF0000"
    fg = color_white_smoke
    return [bg,c1,c2,dup,fg]

# ORANGE THEME
def tema_laranja():
    bg     = color_grey_deep # na verdade isso é um cinza
    c1   = color_grey_medium # na verdade isso é um cinza
    c2 = "#FD7014"
    dup  = "#EEEEEE"
    fg = color_white_smoke
    return [bg,c1,c2,dup,fg]

# CIAN THEME
def tema_ciano():
    bg       = color_grey_deep
    c1     = color_grey_medium
    c2   = "#00ADB5"
    dup    = "#00FFF5"
    fg = color_white_smoke
    return [bg,c1,c2,dup,fg]

# PURPLE THEME
def tema_roxo():
    bg     = color_black
    c1   = "#3E065F"
    c2 = "#700B97"
    dup  = "#8E05C2"
    fg = color_white_smoke
    return [bg,c1,c2,dup,fg]

# mapa de cores do jogo
def mapa_de_cores():
    padrao1 = [1,1,1,2,2,2,1,1,1]
    padrao2 = [2,2,2,1,1,1,2,2,2]
    return [padrao1,padrao1,padrao1,padrao2,padrao2,padrao2,padrao1,padrao1,padrao1]

def alterar_tema_original(tema):
      
    return tema

def cor_de_alerta():
    return tema_vermelho()[3]
    

def lista_de_temas():
    return ['tema_rosa','tema_vermelho','tema_laranja','tema_ciano','tema-roxo']

def pega_cor(linha,coluna):
    mapa = mapa_de_cores()
    ref_cor_de_fundo = mapa[linha][coluna]
    return tema_laranja()[ref_cor_de_fundo +1]

def pintar_tabuleiro():
    for nlinha , linha in enumerate(mapa_de_cores()):
        for ncoluna , coluna in enumerate(linha):
            celula = mapa_botoes[ nlinha * 9 + ncoluna]
            selBG = pega_cor(nlinha,ncoluna)
            celula.configure(bg=selBG)

def pintar_duplicidades(tabuleiro):
    for nlinha , linha in enumerate(tabuleiro):
        for ncoluna , valor in enumerate(linha):
            celula = mapa_botoes[ nlinha * 9 + ncoluna]
            bDuplicicdade = checar_duplicidades(valor,nlinha,ncoluna,tabuleiro)
            if (valor != 0 and bDuplicicdade):
                celula.configure(bg=cor_de_alerta())
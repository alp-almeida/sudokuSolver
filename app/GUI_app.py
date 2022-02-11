
import tkinter as tk  # usada para criação da interface de usuário

import configure as cfg  # possui regras e detalhes do jogo.
from globals import *  # importa os mapas usados para configurar o jogo
from GUI_assembling import *
from GUI_config import *  # configurações da interface de usuário.
from GUI_themes import *  # definições e funções para alteração do tema do jogo.
from strings import *
from sudoku_back_app import *  # possui regras e detalhes do jogo.
import solver

def _on_key_pressed(event):
    entrada = event.char
    if (entrada in ['1','2','3','4','5','6','7','8','9','0']):
        num = int(entrada)
        pega_posicao_botao(text_var=  num , local= area_botoes, local_name=FRAME_ENTRADAS)

# Definindo o tema de início.
bg,c1,c2,dup,fg = tema_ciano()



# GUI:
app = tk.Tk()
app.title(STR_TITULO_GUI)
app.geometry(f'{GUI_WIDTH}x{GUI_HEIGHT}')
app.configure(bg=bg)
app.bind(sequence="<Key>", func=_on_key_pressed)

# area do menu
area_menu = tk.Frame(app)
area_menu.configure(bg=bg)
area_menu.pack()

btn_solver = tk.Button(area_menu)
btn_solver.configure(text='Solver')
#btn_solver.configure(width=2)
#btn_solver.configure(height= 10)
btn_solver.configure(command= lambda: solver.percorrer_tabuleiro())
btn_solver.configure(pady=1 , padx=1)
btn_solver.configure(state=tk.NORMAL)
btn_solver.configure(font="-family helvetica -size 12")
btn_solver.grid(row=0,column=0)

# areas internas do jogo

# area onde ficarão os botões do tabuleiro
area_tabuleiro = tk.Frame(app)
area_tabuleiro.configure(width=GUI_WIDTH , height=GUI_HEIGHT)
area_tabuleiro.configure(bg=bg)
area_tabuleiro.configure(pady=10)
area_tabuleiro.pack()

# area onde ficarão os botões de entrada
area_botoes = tk.Frame(app)
area_botoes.configure(bg=bg)
area_botoes.pack()

rgCampos = range(0,9)

for linha in rgCampos:
    for coluna in rgCampos:
        myTextVar = tabuleiro[linha][coluna]
        cell = criar_botao(local= area_tabuleiro, text_var= myTextVar, linha=linha, coluna=coluna , local_name=FRAME_TAB)
        cell.grid(column=coluna , row=linha)
        mapa_botoes.append(cell)

tk.Label(area_botoes,text="Entradas", bg=bg , fg=fg, pady = 6).grid(row=0,columnspan=10)
for entrada in cfg.ENTRADA_OP:
    btn = criar_botao(local= area_botoes, text_var= entrada, linha=0, coluna=entrada, local_name=FRAME_ENTRADAS)
    btn.grid(row=1,column=entrada)

pintar_tabuleiro()
pintar_duplicidades(tabuleiro)
app.mainloop() # Aqui inicia a execução do jogo

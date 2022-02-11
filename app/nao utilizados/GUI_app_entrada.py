# app configuration

from strings import *
from GUI_config import *

# GUI tech imports
import tkinter as tk
from tkinter import Button, Variable, Widget, ttk


# game imports
import testing as tb
import configure as cfg
import sys

tabuleiro = tb.TABULEIRO_ORIGINAL




# GUI:
app = tk.Tk()
app.title(STR_TITULO_GUI_ENTRADA)
app.geometry("40x300")
app.configure(bg=COLOR_WHITE_SMOKE)
b = {}

"""
def retorna_valor(text):
    print(text)

def criar_botao(text_var):
    name_var = "btn{0}".format(text_var)
    btn = tk.Button(app,text=text_var, name=name_var, command=lambda: retorna_valor(text_var))
    return btn

for entrada in cfg.ENTRADA_OP:
    btn1 = criar_botao(entrada)
    btn1.pack()"""


app.mainloop()











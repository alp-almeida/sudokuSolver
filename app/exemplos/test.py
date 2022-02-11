# area com as opções do confguração


#menu

menu = tk.Frame(app)
menu.configure(width=GUI_WIDTH, height=40)
menu.configure(padx=10, pady=10)
menu.pack(fill='x')


#seletor de temas
seletor_de_temas = ttk.Combobox(menu,)
seletor_de_temas.configure(height= int(menu.cget('height')))
seletor_de_temas.configure(values= lista_de_temas())
seletor_de_temas.pack(side='left')
# CONTINUAR A DESVENDAR COMO COLOCAR UM CAMANDO NO COMBOBOX




def muda_tema():
    selecao = seletor_de_temas.get()
    if (selecao != STR_COMBO_BOX_TEMA):
        bg,c1,c2,dup,fg = locals()[selecao]
        pintar_tabuleiro()
        pintar_duplicidades()

btn_sdt = ttk.Button(menu)
btn_sdt.configure(text='Tema')
btn_sdt.configure(command=muda_tema)
btn_sdt.pack()
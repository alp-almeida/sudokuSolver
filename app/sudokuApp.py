import sudoku_back_app as b
import sudoku_back_vitoria as v


def main():
    tabuleiro = b.criar_tabuleiro()
    tabuleiro[0][0] = 45
    tabuleiro[0][8] = 30
    v.regra_da_vitoria(tabuleiro)
    
    b.mostrar_tabuleiro(tabuleiro)
    v.vitoria_soma_quadrados(tabuleiro)



# aqui executa o aplicativo
main()

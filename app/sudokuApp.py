import sudoku_back_app as b
import sudoku_back_vitoria as v


def main():
    tabuleiro = b.criar_tabuleiro()
    tabuleiro[8][0] = 45
    
    print v.vitoria_soma_linha(tabuleiro)




# aqui executa o aplicativo
main()

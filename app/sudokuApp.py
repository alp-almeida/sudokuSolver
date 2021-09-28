import sudoku_back_app as b
import sudoku_back_vitoria as v


def main():
    tabuleiro = b.criar_tabuleiro()
    tabuleiro[8][0] = 45
    tabuleiro[0][8] = 30
    v.regra_da_vitoria(tabuleiro)
    
    print tabuleiro[0][6:9]




# aqui executa o aplicativo
main()

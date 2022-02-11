from sudoku_back_app import *
from sudoku_back_vitoria import *

TABULEIRO_ORIGINAL = entrada_tabuleiro (  [ 0,0,3,0,0,4,5,0,2,
                                            0,5,0,0,0,3,0,0,0,
                                            0,0,8,0,0,5,3,6,0,
                                            0,0,0,2,0,0,7,4,3,
                                            2,7,0,3,0,0,0,8,0,
                                            3,4,0,7,5,0,0,0,0,
                                            0,0,5,4,0,0,0,0,6,
                                            9,0,2,0,0,0,0,5,0,
                                            4,0,0,0,0,2,9,0,0  ],
                                            criar_tabuleiro())

GABARITO           = entrada_tabuleiro (    [ 7,9,3,8,6,4,5,1,2,
                                              6,5,4,1,2,3,8,9,7,
                                              1,2,8,9,7,5,3,6,4,
                                              5,8,6,2,1,9,7,4,3,
                                              2,7,9,3,4,6,1,8,5,
                                              3,4,1,7,5,8,6,2,9,
                                              8,3,5,4,9,1,2,7,6,
                                              9,1,2,6,3,7,4,5,8,
                                              4,6,7,5,8,2,9,3,1 ],
                                            criar_tabuleiro())

#print(regra_da_vitoria(GABARITO))




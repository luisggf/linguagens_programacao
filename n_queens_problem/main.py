from auxiliar import *

empty_board = generate_table()
Queen_Problem_Class_Instance = Queens(empty_board)
try:
    solved_board = Queen_Problem_Class_Instance.solve_n_queen()
    display_chessboard(solved_board)
except Exception as e:
    print("Erro: ", e)

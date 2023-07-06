import math
import sys
import random
sys.path.append('../sudoku') 
import funcObjetivo
#import sudoku

import random

def semi_greedy_algorithm(sudoku, k):
    violations = funcObjetivo.func_objetivo(sudoku)

    # passa por todas as celulas vazias
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                moves = []
                for num in range(1, 10):
                    sudoku[i][j] = num
                    new_violations = funcObjetivo.func_objetivo(sudoku)
                    moves.append((i, j, num, new_violations))
                sudoku[i][j] = 0  # desfaz tentativa de troca

                if moves:
                    top_moves  = []
                    moves.sort(key=lambda x: x[3])
                    sliceqnt = int(math.ceil(len(moves)* (k/100)))

                    top_moves= moves[:sliceqnt]
                    
                    random_move = random.choice(top_moves)
                    i, j, num, violations_num  = random_move
                    sudoku[i][j] = num
                    violations = funcObjetivo.func_objetivo(sudoku)

    return sudoku, violations
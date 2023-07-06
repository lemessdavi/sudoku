import sys
import random
sys.path.append('../sudoku')  
import funcObjetivo 
import utils
from semigreedy.semigreedy_random import semi_greedy_algorithm
from buscalocal.buscaLocalSimplesMA import local_search_algorithm

def local_search_grasp(sudoku):

    positions_editable = utils.search_empty_positions(sudoku)

    #construcao aleatoria
    best_sudoku = utils.random_fill(sudoku)

    best_violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while best_violations > 0 and iterations < 10:
        
        new_sudoku, new_violations = semi_greedy_algorithm(sudoku, 15)
        new_sudoku, new_violations = local_search_algorithm(new_sudoku, positions_editable)

        if best_violations > new_violations:
            best_sudoku = new_sudoku
            best_violations = new_violations

        iterations += 1

    return best_sudoku, best_violations

def printSudoku(sudoku): 
    print()
    print()
    print()

    for row in sudoku:
        print(row)

    print()

sudokinho = [
    [0, 6, 0, 9, 0, 0, 3, 7, 2],
    [3, 9, 8, 7, 0, 6, 4, 1, 5],
    [2, 0, 7, 1, 3, 0, 0, 8, 9],
    [0, 0, 6, 0, 1, 0, 0, 3, 8],
    [0, 0, 0, 2, 5, 3, 0, 0, 1],
    [0, 0, 0, 8, 6, 7, 0, 9, 4],
    [0, 0, 3, 5, 9, 2, 1, 0, 6],
    [0, 0, 9, 6, 0, 1, 8, 0, 0],
    [6, 0, 2, 3, 0, 0, 0, 5, 7]
]

result, num_violations = local_search_grasp(sudokinho)

printSudoku(result)
print("Número de violações:", num_violations)
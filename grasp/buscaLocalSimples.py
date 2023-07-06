import sys
import random
sys.path.append('../sudoku')  
import funcObjetivo 
import utils
from semigreedy.semigreedy_random import semi_greedy_algorithm
from buscalocal.buscaLocalSimplesMA import local_search_algorithm

def local_search_grasp(sudoku, max_iterations):

    positions_editable = utils.search_empty_positions(sudoku)

    #construcao aleatoria
    best_sudoku = utils.random_fill(sudoku)

    best_violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while best_violations > 0 and iterations < max_iterations:
        
        new_sudoku, new_violations = semi_greedy_algorithm(sudoku, 10)
        new_sudoku, new_violations = local_search_algorithm(new_sudoku, 10, positions_editable)

        if best_violations > new_violations:
            best_sudoku = new_sudoku
            best_violations = new_violations

        iterations += 1

    return best_sudoku, best_violations
import sys
sys.path.append('../sudoku')  
import funcObjetivo 
import utils
from semigreedy.semigreedy_random import semi_greedy_algorithm
from buscalocal.buscaLocalIterada import iterated_local_search_algorithm

def iterated_local_search_grasp(sudoku, p, max_iterations, I):

    positions_editable = utils.search_empty_positions(sudoku)

    #construcao aleatoria
    best_sudoku = utils.random_fill(sudoku)

    best_violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while best_violations > 0 and iterations < (max_iterations - (max_iterations * I/100)):
        
        new_sudoku, new_violations = semi_greedy_algorithm(sudoku, 10)
        new_sudoku, new_violations = iterated_local_search_algorithm(new_sudoku, p, max_iterations * I/100, positions_editable)

        if best_violations > new_violations:
            best_sudoku = new_sudoku
            best_violations = new_violations

        iterations += 1

    return best_sudoku, best_violations
import sys
import random
from collections import Counter
sys.path.append('C:\GitHub\sudoku') 
import utils
from buscalocal.buscaLocalSimplesMA import local_search_algorithm

def iterated_local_search_algorithm(sudoku, p):

    positions_editable = utils.search_empty_positions(sudoku)
    sudoku = utils.random_fill(sudoku)
    sudoku, violations = local_search_algorithm(sudoku, positions_editable)
    
    iterations = 0

    while violations > 0 and iterations < 100:
        
        aux_positions_editable = positions_editable.copy()

        #perturbacao
        new_sudoku = sudoku.copy()
        perturbacao = 0

        while perturbacao < p:
            ai, aj = random.choice(aux_positions_editable)
            aux_positions_editable.remove((ai, aj))
            bi, bj = random.choice(aux_positions_editable)
            aux_positions_editable.remove((bi, bj))

            #swap
            new_sudoku[ai][aj], new_sudoku[bi][bj] = new_sudoku[bi][bj], new_sudoku[ai][aj]

            perturbacao += 1

        new_sudoku, new_violations = local_search_algorithm(new_sudoku, positions_editable)

        if violations > new_violations:
            sudoku = new_sudoku.copy()
            violations = new_violations

        iterations += 1

    return sudoku, violations

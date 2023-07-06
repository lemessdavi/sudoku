import sys
import random
from collections import Counter
sys.path.append('C:\GitHub\sudoku') 
import funcObjetivo
from buscalocal.buscaLocalSimplesMA import local_search_algorithm

def iterated_local_search_algorithm(sudoku, p, max_iterations, positions_editable = []):

    if len(positions_editable) < 1:
        len_matrix = len(sudoku)

        #quantos tem de cada numero
        numbers = Counter(item for row in sudoku for item in row if item != 0)
        #quantos faltam de cada numero
        numbers = {key: len_matrix - count for key, count in numbers.items()}

        #marca as posicoes editaveis e preenche
        for i in range(len(sudoku)):
            for j in range(len(sudoku[i])):
                #se a posicao estiver vazia
                if sudoku[i][j] == 0:
                    #salva a posicao atual em posicoes editaveis
                    positions_editable.append((i, j))

                    #popula aleatoriamente a posicao atual
                    index, qtd = random.choice(list(numbers.items()))
                    sudoku[i][j] = index
                    numbers[index] -= 1
                    if numbers[index] < 1:
                        numbers.pop(index)

    violations = funcObjetivo.func_objetivo(sudoku)

    sudoku, violations = local_search_algorithm(sudoku, positions_editable)
    
    iterations = 0

    while violations > 0 and iterations < max_iterations:
        
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

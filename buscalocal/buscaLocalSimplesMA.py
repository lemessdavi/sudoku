import sys
import random
from collections import Counter
sys.path.append('C:\GitHub\sudoku') 
import funcObjetivo

def local_search_algorithm(sudoku, max_iterations, positions_editable = []):

    #se o sudoku já está preenchido, deverá mandar as posicoes editaveis para o sudoku
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
    iterations = 0

    while violations > 0 and iterations < max_iterations:
        
        positions_editable_aux = positions_editable.copy()
        best_possible = []

        #gera vizinhanca
        while len(positions_editable_aux) > 1:
            #seleciona duas posicoes aleatorias e remove as posicoes pra nao serem mais selecionadas
            ai, aj = random.choice(positions_editable_aux)
            positions_editable_aux.remove((ai, aj))
            bi, bj = random.choice(positions_editable_aux)
            positions_editable_aux.remove((bi, bj))

            #swap
            sudoku[ai][aj], sudoku[bi][bj] = sudoku[bi][bj], sudoku[ai][aj]

            #calcula funcao objetivo para vizinho
            violations_new = funcObjetivo.func_objetivo(sudoku)

            #se é uma melhoria
            if violations > violations_new:
                #adiciona posicoes no array de possiveis melhoras
                best_possible.append((ai, aj, bi, bj))

            #desfaz swap
            sudoku[ai][aj], sudoku[bi][bj] = sudoku[bi][bj], sudoku[ai][aj]

        if len(best_possible) > 0:
            #seleciona aleatoriamente um possivel melhora
            best_move = random.choice(best_possible)

            #faz o swap
            sudoku[best_move[0]][best_move[1]], sudoku[best_move[2]][best_move[3]] = sudoku[best_move[2]][best_move[3]], sudoku[best_move[0]][best_move[1]]
            violations = funcObjetivo.func_objetivo(sudoku)


        iterations += 1

    return sudoku, violations
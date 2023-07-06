from collections import Counter
import sys
import random
sys.path.append('../sudoku') 
import funcObjetivo
import random


def iterated_greedy_algorithm(sudoku, k, D, max_iterations ,indices_vazios = []):
    violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

     #se o sudoku já está preenchido, deverá mandar as posicoes editaveis para o sudoku
    if len(indices_vazios) < 1:
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
                    indices_vazios.append((i, j))

                    #popula aleatoriamente a posicao atual
                    index, qtd = random.choice(list(numbers.items()))
                    sudoku[i][j] = index
                    numbers[index] -= 1
                    if numbers[index] < 1:
                        numbers.pop(index)

    violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while violations > 0 and iterations < max_iterations:
        random.shuffle(indices_vazios)

        for i in range(D):
            row, col = indices_vazios[i]
            sudoku[row][col] = 0

        # passa por todas as celulas vazias
        for i,j in indices_vazios:
            moves = []
            for num in range(1, 10):
                sudoku[i][j] = num
                new_violations = funcObjetivo.func_objetivo(sudoku)
                moves.append((i, j, num, new_violations))
            sudoku[i][j] = 0  # desfaz tentativa de troca

            if moves:
                top_moves  = []
                moves.sort(key=lambda x: x[3]) #ordena por violacoes decrescente
                sliceqnt = int(len(moves)* (k/100))
                top_moves= moves[:sliceqnt]
                
                random_move = random.choice(top_moves)
                i, j, num, violations_num  = random_move
                sudoku[i][j] = num
                violations = funcObjetivo.func_objetivo(sudoku)

        iterations += 1

    return sudoku, violations
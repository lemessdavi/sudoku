import sys
import random
sys.path.append('/Users/lemes/Documents/Sudoku/sudoku') 
import funcObjetivo
import random


def iterated_greedy_algorithm(sudoku, k, D):
    violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    #guarda todos as celulas que podem ser destruidas depois
    indices_vazios = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                indices_vazios.append((i, j))

    while violations > 0 and iterations < 1000:
        random.shuffle(indices_vazios)

        if iterations != 0:
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


sudukinho = [
[0, 6, 0, 9, 0, 0, 3, 7, 2],
[3, 9, 8, 7, 0, 6, 4, 1, 5],
[2, 0, 7, 1, 3, 0, 0, 8, 9],
[0, 0, 6, 0, 1, 0, 0, 3, 8],
[0, 0, 0, 2, 5, 3, 0, 0, 1],
[0, 0, 0, 8, 6, 7, 0, 9, 4],
[0, 0, 3, 5, 9, 2, 1, 0, 6],
[0, 0, 9, 6, 0, 1, 8, 0, 0],
[6, 0, 2, 3, 0, 0, 0, 5, 7]]

for row in sudukinho:
    print(row)

print()

result, num_violations = iterated_greedy_algorithm(sudukinho, 15, 30)

print()

for row in result:
    print(row)

print()

print("Número de violações:", num_violations)
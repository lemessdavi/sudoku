import sys
import random
sys.path.append('/Users/lemes/Documents/Sudoku/sudoku') 
import funcObjetivo
import sudoku

def local_search_random(sudoku):
    violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while violations > 0 and iterations < 1000:
        min_violations = float('inf')
        best_moves = []

        # percorre todas as células vazias no Sudoku
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    possible_moves = []
                    for num in range(1, 10):
                        sudoku[i][j] = num
                        new_violations = funcObjetivo.func_objetivo(sudoku)
                        if new_violations < min_violations:
                            min_violations = new_violations
                            possible_moves = [(i, j, num)]
                        elif new_violations == min_violations:
                            possible_moves.append((i, j, num))
                    sudoku[i][j] = 0  # desfaz tentativa de troca
                    
                    if possible_moves:
                        best_moves.append(random.choice(possible_moves)) #pega aleatoriamente os melhores movimentos

        # escolhe aleatoriamente uma das melhores opções
        if best_moves:
            i, j, num = random.choice(best_moves)
            sudoku[i][j] = num
            violations = min_violations

        iterations += 1

    return sudoku, violations


sudukinho = [[0, 6, 0, 9, 0, 0, 3, 7, 2],
[3, 9, 8, 7, 0, 6, 4, 1, 5],
[2, 0, 7, 1, 3, 0, 0, 8, 9],
[0, 0, 6, 0, 1, 0, 0, 3, 8],
[0, 0, 0, 2, 5, 3, 0, 0, 1],
[0, 0, 0, 8, 6, 7, 0, 9, 4],
[0, 0, 3, 5, 9, 2, 1, 0, 6],
[0, 0, 9, 6, 0, 1, 8, 0, 0],
[6, 0, 2, 3, 0, 0, 0, 5, 7]]

#result, num_violations = local_search_random(sudoku.playable_sudoku)
result, num_violations = local_search_random(sudukinho)

print()
print()
print()

for row in result:
    print(row)

print()

print("Número de violações:", num_violations)
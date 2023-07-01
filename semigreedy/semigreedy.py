import sys
import random
sys.path.append('/Users/lemes/Documents/Sudoku/sudoku') 
import funcObjetivo
import sudoku

import random

def semi_greedy_algorithm(sudoku):
    violations = funcObjetivo.func_objetivo(sudoku)

    while violations > 0:
        min_violations = float('inf')

        # passa por todas as celulas vazias
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    top_moves = []
                    for num in range(1, 10):
                        sudoku[i][j] = num
                        new_violations = funcObjetivo.func_objetivo(sudoku)
                        top_moves.append((i, j, num, new_violations))
                    sudoku[i][j] = 0  # desfaz tentativa de troca

                    if top_moves:
                        top_moves.sort(key=lambda x: x[4], descending=True)
                        top_moves = top_moves
                        random_move = random.choice(top_moves)
                        i, j, num = random_move
                        sudoku[i][j] = num

        violations = min_violations

        if i == 8 and j == 8:
            break



result, num_violations = semi_greedy_algorithm(sudoku.playable_sudoku)

print()
print()
print()

for row in result:
    print(row)

print()

print("Número de violações:", num_violations)
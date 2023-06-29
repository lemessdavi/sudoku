import sys
sys.path.append('/Users/lemes/Documents/Sudoku/sudoku') 
import funcObjetivo
import sudoku

def greedy_algorithm(sudoku):
    violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while violations > 0 and iterations < 1000:
        min_violations = float('inf')
        best_move = None

        # Percorrer todas as posições vazias no Sudoku
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    for num in range(1, 10):
                        sudoku[i][j] = num
                        new_violations = funcObjetivo.func_objetivo(sudoku)
                        if new_violations < min_violations:
                            min_violations = new_violations
                            best_move = (i, j, num)
                    sudoku[i][j] = 0  # Desfazer a tentativa

        # Atualizar o Sudoku com o movimento que reduziu as violações
        if best_move is not None:
            i, j, num = best_move
            sudoku[i][j] = num
            violations = min_violations

        iterations += 1

    return sudoku, violations


result, num_violations = greedy_algorithm(sudoku.playable_sudoku)

print()
print()
print()

for row in result:
    print(row)

print()

print("Número de violações:", num_violations)

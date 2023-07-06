import sys
sys.path.append('../sudoku') 
import funcObjetivo
import sudoku

def get_empty_cells(sudoku):
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def count_possible_options(sudoku, cell):
    i, j = cell
    options = set(range(1, 10))

    # Verificar as opções possíveis na linha
    options -= set(sudoku[i])

    # Verificar as opções possíveis na coluna
    column = [row[j] for row in sudoku]
    options -= set(column)

    # Verificar as opções possíveis no quadrante
    quadrant_row = (i // 3) * 3
    quadrant_col = (j // 3) * 3
    for row in range(quadrant_row, quadrant_row + 3):
        for col in range(quadrant_col, quadrant_col + 3):
            options.discard(sudoku[row][col])

    return options

def greedy_algorithm(sudoku):
    violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while violations > 0 and iterations < 1000:
        min_violations = float('inf')
        best_move = None
        empty_cells = get_empty_cells(sudoku)

        # Percorrer as células vazias com o menor número de opções disponíveis
        for cell in empty_cells:
            options = count_possible_options(sudoku, cell)
            if len(options) == 1:
                # Se houver apenas uma opção possível, atribuir imediatamente
                i, j = cell
                num = options.pop()
                sudoku[i][j] = num
                violations = funcObjetivo.func_objetivo(sudoku)
                break
            elif len(options) > 1:
                if len(options) < min_violations:
                    min_violations = len(options)
                    best_move = (cell, options)

        if best_move is not None:
            cell, options = best_move
            i, j = cell
            for num in options:
                sudoku[i][j] = num
                new_violations = funcObjetivo.func_objetivo(sudoku)
                if new_violations < min_violations:
                    min_violations = new_violations
                    best_move = (cell, num)
            sudoku[i][j] = 0  # Desfazer a tentativa

        # Atualizar o Sudoku com o movimento que reduziu as violações
        if best_move is not None:
            cell, num = best_move
            i, j = cell
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

def func_objetivo(sudoku):
    violations = 0  # Contador de violações

    # Verificar as violações nas linhas
    for row in sudoku:
        unique_elements = set(row)
        violations += len(row) - len(unique_elements)

    # Verificar as violações nas colunas
    for col in range(9):
        column = [row[col] for row in sudoku]
        unique_elements = set(column)
        violations += len(column) - len(unique_elements)

    # Verificar as violações nos quadrantes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrant = []
            for k in range(3):
                for l in range(3):
                    quadrant.append(sudoku[i+k][j+l])
            unique_elements = set(quadrant)
            violations += len(quadrant) - len(unique_elements)

    # Contar os zeros como violações
    for row in sudoku:
        violations += row.count(0)

    return violations

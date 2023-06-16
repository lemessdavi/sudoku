import random

def generate_sudoku():
    # cria a matriz gabarito zerada
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # preenche a matriz gabarito
    fill_sudoku(sudoku, 0, 0)

    # copia a matriz gabarito
    sudoku_with_zeros = [[sudoku[row][col] for col in range(9)] for row in range(9)]

    # cria o puzzle
    remove_numbers(sudoku_with_zeros, 45)

    return sudoku, sudoku_with_zeros

def fill_sudoku(sudoku, row, col):
    # ve final da coluna
    if col == 9:
        row += 1
        col = 0

    # ve final da matriz
    if row == 9:
        return True

    numbers = random.sample(range(1, 10), 9)

    for num in numbers:
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num

            # preenche prox espaco da matriz
            if fill_sudoku(sudoku, row, col + 1):
                return True

            # se da pra preencher, apaga esse espaço e tenta o proximo numero
            sudoku[row][col] = 0

    # se nenhum numero puder nessa posicao
    return False

def is_valid(sudoku, row, col, num):
    # verifica se tem o numero na mesma linha ou coluna
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    # verifica se tem o numero no mesmo 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def remove_numbers(sudoku , num_to_remove):
    # remove aleatorio se descomentar
    # num_to_remove = random.randint(40, 50)

    # remove numeros aleatorios ate a qnt escolhida
    for _ in range(num_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        sudoku[row][col] = 0

complete_sudoku, playable_sudoku = generate_sudoku()

print()
print()

print("Sudoku Completo:")
for row in complete_sudoku:
    print(row)

print()
print()

print("Sudoku Jogável:")
for row in playable_sudoku:
    print(row)

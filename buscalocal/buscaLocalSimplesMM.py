import sys
import random
sys.path.append('C:\GitHub\sudoku') 
import funcObjetivo

def local_search(sudoku):

    len_matrix = len(sudoku)

    #quantos tem de cada numero
    # numbers = {j:len_matrix - i.count(j) for i in sudoku for j in i if j != 0 and len_matrix - i.count(j) > 0}
    numbers = {}
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            posicao = sudoku[i][j]
            if posicao > 0:
                if posicao not in numbers:
                    numbers[posicao] = len_matrix - 1
                else:
                    numbers[posicao] -= 1

    positions_editable = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                #salva posicoes editaveis
                positions_editable.append((i, j))

                #popula aleatoriamente
                index, qtd = random.choice(list(numbers.items()))
                sudoku[i][j] = index
                numbers[index] -= 1
                if numbers[index] < 1:
                    numbers.pop(index)
                print(index, numbers)

    violations = funcObjetivo.func_objetivo(sudoku)
    iterations = 0

    while violations > 0 and iterations < 1000:
        
        positions_editable_aux = positions_editable.copy() #ver se funciona
        sudoku_aux = sudoku.copy() #ver se funciona

        best_sudoku = sudoku.copy()
        best_violations = violations.copy()

        #gera vizinhanca
        while len(positions_editable_aux) > 2:
            #pega a primeira posicao aleatoria
            ai, aj = random.choice(positions_editable_aux)

            #remove a posicao pra nao ser mais selecionada
            positions_editable_aux.remove((ai, aj))

            #pega a segunda posicao aleatoria
            bi, bj = random.choice(positions_editable_aux)

            #remove a posicao pra nao ser mais selecionada
            positions_editable_aux.remove((bi, bj))

            #swap
            sudoku_aux[ai][aj] = sudoku_aux[bi][bj]

            #calcula funcao objetivo para vizinho
            violations_new = funcObjetivo.func_objetivo(sudoku_aux)

            #se o vizinho é melhor que o original e melhor que o melhor atual
            if violations_new < violations and violations_new < best_violations:
                #atualiza melhor atual
                best_violations = violations_new
                best_sudoku = sudoku_aux

        sudoku = best_sudoku
        violations = best_violations

        iterations += 1

    return sudoku, violations


sudokinho = [
    [0, 6, 0, 9, 0, 0, 3, 7, 2],
    [3, 9, 8, 7, 0, 6, 4, 1, 5],
    [2, 0, 7, 1, 3, 0, 0, 8, 9],
    [0, 0, 6, 0, 1, 0, 0, 3, 8],
    [0, 0, 0, 2, 5, 3, 0, 0, 1],
    [0, 0, 0, 8, 6, 7, 0, 9, 4],
    [0, 0, 3, 5, 9, 2, 1, 0, 6],
    [0, 0, 9, 6, 0, 1, 8, 0, 0],
    [6, 0, 2, 3, 0, 0, 0, 5, 7]
]

result, num_violations = local_search(sudokinho)

print()
print()
print()

for row in result:
    print(row)

print()

print("Número de violações:", num_violations)
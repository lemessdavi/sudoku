import sys
sys.path.append('../sudoku') 
import funcObjetivo
#import sudoku

def greedy_algorithm(sudoku):
    violations = funcObjetivo.func_objetivo(sudoku)

    min_violations = float('inf')
    best_move = None

    # passa por todas as celulas vazias
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1, 10):
                    sudoku[i][j] = num
                    new_violations = funcObjetivo.func_objetivo(sudoku)
                    if new_violations < min_violations:
                        min_violations = new_violations
                        best_move = (i, j, num)
                    sudoku[i][j] = 0  # desfaz tentativa de troca
                
                # bota o numero com menos viloacoes
                if best_move is not None:
                    i, j, num = best_move
                    sudoku[i][j] = num
                    violations = min_violations
                    
    return sudoku, violations

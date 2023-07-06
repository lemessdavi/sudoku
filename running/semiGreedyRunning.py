import sys
sys.path.append('../sudoku')
import utils
from semigreedy.semigreedy_random import semi_greedy_algorithm

for i in range(1, 11):
    sudoku = utils.read_instance(i)
    violations = 0

    for j in range(10):
        new_violations, new_sudoku = semi_greedy_algorithm(sudoku, 15)
        violations += new_violations

    violations = violations/10
    print('Instância nº ' + str(i) + ' - Média de violações: ' + str(violations))

import sys
sys.path.append('../sudoku')
import utils
from grasp.iteratedGreedy import grasp_iterated_greedy_algorithm

for i in range(1, 11):
    violations = 0

    for j in range(10):
        new_sudoku, new_violations = grasp_iterated_greedy_algorithm(utils.read_instance(i), 15, 30)
        violations += new_violations

    violations = violations/10
    print('Instância nº ' + str(i) + ' - Média de violações: ' + str(violations))

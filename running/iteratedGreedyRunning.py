import sys
sys.path.append('../sudoku')
import utils
from iteratedgreedy.iteratedgreedy import iterated_greedy_algorithm

for index_instace in range(1, 11):
    violations = 0

    for index_tentativa in range(10):
        new_sudoku, new_violations = iterated_greedy_algorithm(utils.read_instance(index_instace), 15, 10, 100, [])
        violations += new_violations

    violations = violations/10
    print('Instância nº ' + str(index_instace) + ' - Média de violações: ' + str(violations))

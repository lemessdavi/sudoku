import sys
sys.path.append('../sudoku')
import utils
from buscalocal.buscaLocalIterada import iterated_local_search_algorithm

for i in range(1, 11):
    violations = 0

    for j in range(10):
        new_sudoku, new_violations = iterated_local_search_algorithm(utils.read_instance(i), 5, 10, [])
        violations += new_violations

    violations = violations/10
    print('Instância nº ' + str(i) + ' - Média de violações: ' + str(violations))

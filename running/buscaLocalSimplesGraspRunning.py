import sys
sys.path.append('../sudoku')
import utils
from grasp.buscaLocalSimples import local_search_grasp

for i in range(1, 11):
    sudoku = utils.read_instance(i)
    violations = 0

    for j in range(10):
        new_sudoku, new_violations = local_search_grasp(sudoku)
        violations += new_violations

    violations = violations/10
    print('Instância nº ' + str(i) + ' - Média de violações: ' + str(violations))

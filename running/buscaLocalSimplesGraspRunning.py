import sys
sys.path.append('../sudoku')
import utils
from grasp.buscaLocalSimples import local_search_grasp

for i in range(11, 21):
    violations = 0

    for j in range(5):
        new_sudoku, new_violations = local_search_grasp(utils.read_instance(i), 200, 50)
        violations += new_violations

    violations = violations/5
    print('Instância nº ' + str(i) + ' - Média de violações: ' + str(violations))

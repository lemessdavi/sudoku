import sys
sys.path.append('../sudoku')
import sudoku

for i in range(7, 19):
    gabarito, instance = sudoku.generate_sudoku()
    file = open('instances/'+str(i), 'w')
    for linha in instance:
        file.write(', '.join(map(str, linha)) + '\n')
    file.close()
    file = open('instances/gabarito/'+str(i), 'w')
    for linha in gabarito:
        file.write(', '.join(map(str, linha)) + '\n')
    file.close()

import random
from collections import Counter

def search_empty_positions(sudoku):
    return [(i, j) for i in range(len(sudoku)) for j in range(len(sudoku[i])) if sudoku[i][j] == 0]

def count_occurrences(sudoku):
    return Counter(item for row in sudoku for item in row if item != 0)
    
def count_number_missing(sudoku):
    len_matrix = len(sudoku)
    numbers = count_occurrences(sudoku)
    return {key: len_matrix - count for key, count in numbers.items()}

def random_fill(sudoku):
    numbers = count_number_missing(sudoku)
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                index, qtd = random.choice(list(numbers.items()))
                sudoku[i][j] = index
                numbers[index] -= 1
                if numbers[index] < 1:
                    numbers.pop(index)
    return sudoku

def read_instance(index):
    data = []
    file = open('instances/' + str(index), 'r')
    for line in file.readlines():
        line = line.strip()
        if line != '':
            data.append(line.split(', '))
    file.close()
    return data
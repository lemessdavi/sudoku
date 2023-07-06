import random

x = {6: 1, 9: 3, 3: 2, 7: 9, 2: 4, 8: 7, 4: 1, 1: 1, 5: 1}
print(x)
index, qtd = random.choice(list(x.items()))
print(index, qtd)

import random
from tqdm import tqdm

def monty_h(door_num):
    n = random.randrange(1,4)
    if door_num == 1:
        if n == 3:
            return('car')
        elif n == 2:
            return('car')
        elif n == 1:
            return('goat')
    elif door_num == 2:
        if n == 3:
            return('car')
        elif n == 2:
            return('goat')
        elif n == 1:
            return('car')
    elif door_num == 3:
        if n == 3:
            return('goat')
        elif n == 2:
            return('car')
        elif n == 1:
            return('car')

win = []
lose = []

for i in tqdm(range(0, 1000000)):
    m = random.randrange(1,4)
    a = monty_h(m)
    if a == 'car':
        win.append(a)
    elif a == 'goat':
        lose.append(a)


# print(win)
# print(lose)

print('Number of winning the prize =',len(win))
print('Number of losing the prize =', len(lose))

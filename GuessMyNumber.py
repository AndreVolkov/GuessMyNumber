# Guess My Number
import sys
from random import randint
n = randint(1,100)
i = 0

#print(n)
def GMN(x):
    if x == n:
        print('Correct')
        sys.exit()
    elif n > x:
        print('More')
    else:
        print('Less')
    return GMN

while i != 10:
    i = i + 1
    x = int(input('Введите загаданное число:'))
    GMN(x)
print('Game Over')    

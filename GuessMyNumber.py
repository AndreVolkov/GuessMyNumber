# Guess My Number
import sys                                      # импорт библиотеки sys
from random import randint                      # импорт функции randint(получение случайных целых чисел) из библиотеки random. 
n = randint(1,100)                              # в переменную "n" генерируем случайное целое число в диапозоне 1-100 включительно
i = 0                                           # счетчик угадываемых попыток.

#print(n)
def gmn(x):                                     # создаем функцию, которая сравнивает число(х) с числом(n)
    if x == n:                                  # если пользователь ввел число и оно совпало с числом компьютера
        print('Correct')                        # печатаем результат
        sys.exit()                              # этой функцией выходим из программы
    elif n > x:                                 # если число компьютера больше числа пользователя
        print('More')                           # печатаем результат - Более
    else:                                       # в противном случае
        print('Less')                           # печатаем результат - Менее
    return gmn                                  # возврат функции

while i != 10:                                  # цикл while выполняется пока не будет 10 попыток
    i = i + 1                                   # считаем попытки 
    x = int(input('Введите загаданное число:')) # вводим целое число (Попытка угадать)
    gmn(x)                                      # в функцию подставляем введенное число пользователя(х)
print('Game Over')                              # Конец игры, т.к. число попыток 10 и число пользователь не угадал    

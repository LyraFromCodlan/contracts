# Описать функцию Fib(N) целого типа, вычисляющую N-й элемент последовательности чисел Фибоначчи FK, которая описывается следующими формулами:
# F1 = 1,        F2 = 1,        FK = FK−2 + FK−1,    K = 3, 4, … .
# Используя функцию Fib, найти пять чисел Фибоначчи с данными номерами N1, N2, …, N5. 

def calculateFib(N: int):
    val_1, val_2 = 1, 1
    for ind in range(3,N+1):
        temp_val = val_2
        val_2 = val_2 + val_1
        val_1 = temp_val
    return val_2

list_of_input = [11, 12, 13, 14, 15]

print([calculateFib(el) for el in list_of_input])
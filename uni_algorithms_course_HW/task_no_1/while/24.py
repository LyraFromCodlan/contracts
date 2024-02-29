# While24. Дано целое число N (> 1). Последовательность чисел Фибоначчи FK определяется следующим образом:
# F1 = 1,        F2 = 1,        FK = FK−2 + FK−1,    K = 3, 4, … .
# Проверить, является ли число N числом Фибоначчи. Если является, то вывести true, если нет — вывести false. 

n = int(input("Enter N value: "))

fib_first = 1
fib_second = 1

while fib_second<n:
    fib_temp = fib_second
    fib_second = fib_second + fib_first
    fib_first = fib_temp

print(True if fib_second == n else False) 
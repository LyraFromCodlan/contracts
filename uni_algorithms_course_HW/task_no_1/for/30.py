# For30. Дано целое число N (> 1) и две вещественные точки на числовой оси: A, B (A < B). Отрезок [A, B] разбит на N равных отрезков. Вывести H — длину каждого отрезка, а также значения функции F(X) = 1 − sin(X) в точках, разбивающих отрезок [A, B]:
# F(A),    F(A + H),    F(A + 2·H),    …,    F(B).

from math import sin

n = int(input("Enter N value: "))
a = float(input("Enter A value: "))
b = float(input("Enter B value: "))

step = (b-a)/n
# solution 1
# points = [ step * point for point in range(1,N+1)]

# print(', '.join([str(el) for el in points]))
# print(', '.join([str(sin(el+A)) for el in points]))

# solution 2
for point_num in range(1,n+1):
    print([step*point_num, 1-sin(a+step*point_num)],sep=", ")
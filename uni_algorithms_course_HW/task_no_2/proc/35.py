# Описать функцию Fact2(N) вещественного типа, вычисляющую двойной факториал:
# N!! = 1·3·5·…·N,    если N — нечетное;
# N!! = 2·4·6·…·N,    если N — четное

def returnFactOver2(N: int):
    value = 1 if N%2==1 else 2
    for next_val in range(value+2, N+1, 2):
        value = value * next_val
    return value

list_of_input = [1, 2, 3, 4, 5]

print([returnFactOver2(el) for el in list_of_input])
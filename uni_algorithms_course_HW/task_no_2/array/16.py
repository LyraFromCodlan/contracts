# Array16°. Дан массив A размера N. Вывести его элементы в следующем порядке:
# A1,    AN,    A2,    AN−1,    A3,    AN−2,    … .
N = int(input("Enter N value: "))
values = [int(el) for el in input("Enter array of "+str(N)+" values separated by space: ").split()]

for ind in range(0,N//2 if N%2==0 else N//2+1):
    if ind != N//2:
        print(values[ind], end=" ")
        print(values[N-1-ind], end=" ")
    else:
        print(values[ind], end=" ")

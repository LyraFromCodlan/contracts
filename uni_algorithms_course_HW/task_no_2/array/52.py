# Array52. Дан массив A размера N. Сформировать новый массив B того же размера, элементы которого определяются следующим образом:
# BK	 = 	2·AK,	если AK < 5,
#  	 	AK/2	в противном случае.

N = int(input("Enter N value: "))
values = [int(el) for el in input("Enter array of "+str(N)+" values separated by space: ").split()]
new_values = [0 for ind in range(0,N)]

for ind in range(0,N):
    if ind<5:
        new_values[ind] = 2*values[ind]
    else:
        new_values[ind] = values[ind]/2
print(values)
print(new_values)
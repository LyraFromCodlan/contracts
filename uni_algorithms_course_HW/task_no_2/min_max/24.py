# Minmax24. Дано целое число N (> 1) и набор из N чисел. Найти максимальную сумму двух соседних чисел из данного набора. 
N = int(input("Enter N value: "))
values = [int(el) for el in input("Enter array of "+str(N)+" values separated by space: ").split()]

max_sum = values[0]
for ind in range(1,N):
    cur_sum = values[ind]+values[ind-1]
    if max_sum < cur_sum:
        max_sum = cur_sum

print(max_sum)
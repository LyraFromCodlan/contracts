# Minmax10. Дано целое число N и набор из N целых чисел. Найти номер первого экстремального (т. е. минимального или максимального) элемента из данного набора. 
N = int(input("Enter N value: "))
values = [int(el) for el in input("Enter array of "+str(N)+" values separated by space: ").split()]

maximum_ind = 0
minimum_ind = 0

for ind in range(0,N):
    if values[ind]>values[maximum_ind]:
        maximum_ind = ind
    if values[ind]<values[minimum_ind]:
        minimum_ind = ind

print("max and min indexes: "+str(maximum_ind)+"; "+str(minimum_ind)+";")
# Series19°. Дано целое число N (> 1) и набор из N целых чисел. Вывести те элементы в наборе, которые меньше своего левого соседа, и количество K таких элементов. 

n = int(input("Enter N number of elements: "))

series = [float(el) for el in input("Enter array of N elements separated by space: ").split()]

counter = 0

for ind in range(1,n):
    if series[ind]<series[ind-1]:
        print(series[ind], sep=", ")
        counter += 1
print("Number of elements in series = "+str(counter))

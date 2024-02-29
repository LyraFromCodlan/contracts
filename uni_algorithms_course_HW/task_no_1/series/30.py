# Series30°. Даны целые числа K, N, а также K наборов целых чисел по N элементов в каждом наборе. Для каждого набора вывести сумму его элементов. 

values = [int(el) for el in input("Enter numbers of elements K and N separated by space: ").split()]
# solution 1
# series = [[float(el) for el in input("Enter N-number of elements in "+str(ind)+" array separated by space:").split()] for ind in range(0,values[0])]
# print(", ".join([str(sum(el)) for el in series]))

# solution 2
# for series_num in range(0,values[0]):
#     series = [float(el) for el in input("Enter N-number of elements in "+str(series_num)+" series separated by space: ").split()]
#     series_sum = 0
#     for ind in range(0,values[1]):
#         series_sum = series_sum + series[ind]
#     print(series_sum,sep=", ")

# solution 3 
series = [float(el) for el in input("Enter series of all elements separated by space: ").split()]

for series_num in range(0,values[0]):
    series_sum = 0
    for ind in range(0,values[1]):
        series_sum = series_sum + series[series_num*values[1]+ind]
    print(series_sum,sep=", ")
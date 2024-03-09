# Matrix30. Дана матрица размера M × N. В каждом ее столбце найти количество элементов, больших среднего арифметического всех элементов этого столбца. 

def calculateArithmeticalAverage(values: list):
    average = 0
    for value in values:
        average+=value
    return average/len(values)

variables = [int(el) for el in input("Enter M, N values separated by space: ").split()]
matrix = []
averages = []
result = [0 for digit in range(0,variables[0])]
for ind in range(0,variables[0]):
    matrix.append([float(el) for el in input("Enter array of "+str(variables[1])+" elements for column "+str(ind)+" separated by space: ").split()])
    averages.append(calculateArithmeticalAverage(matrix[ind]))
    for el in matrix[ind]:
        if el>averages[ind]:
            result[ind]+=1

print("; ".join([str(el) for el in result]))
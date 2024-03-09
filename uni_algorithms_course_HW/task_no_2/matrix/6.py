# Matrix6. Даны целые положительные числа M, N, число D и набор из N чисел. Сформировать матрицу размера M × N, у которой первая строка совпадает с исходным набором чисел, а элементы каждой следующей строки равны соответствующему элементу предыдущей строки, умноженному на D (в результате каждый столбец матрицы будет содержать элементы геометрической прогрессии). 

# # long solution

# variables = [int(el) for el in input("Enter M, N, D values separated by space: ").split()]
# values = [float(el) for el in input("Enter array of "+str(variables[1])+" elements separated by space: ").split()]

# M = variables[0]
# N = variables[1]
# D = variables[2]
# matrix = [values]

# for ind in range(1,M):
#     matrix.append([el*D for el in matrix[ind-1]])

# print('\n'.join([' '.join([str(el) for el in array]) for array in matrix]))

# # shortened solution

variables = [int(el) for el in input("Enter M, N, D values separated by space: ").split()]
matrix = [[float(el) for el in input("Enter array of "+str(variables[1])+" elements separated by space: ").split()]]

for ind in range(1,variables[0]):
    matrix.append([el*variables[2] for el in matrix[ind-1]])

print('\n'.join([' '.join([str(el) for el in array]) for array in matrix]))
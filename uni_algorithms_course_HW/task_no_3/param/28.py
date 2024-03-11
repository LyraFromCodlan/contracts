# Param28. Описать процедуру RemoveRowCol(A, M, N, K, L), удаляющую из вещественной матрицы A размера M × N строку и столбец, которые содержат элемент AK,L (предполагается, что M > 1 и N > 1; если K > M или L > N, то матрица не изменяется). Двумерный массив A и числа M, N являются входными и выходными параметрами. Дана матрица A размера M × N и числа K, L. Применить к матрице A процедуру RemoveRowCol и вывести размер полученной матрицы и ее элементы. 

# this is used to allow predefinition of variable as matrix which in this case is a lisr of lists
from typing import List

def removeRowCol(matrix : List[list], m : int, n : int, k : int, l : int):
    if k > m or l > n:
        return matrix
    else:
        for ind in range(0, m):
            del matrix[ind][l-1]
        del matrix[k-1]
        return matrix
    


values = [int(el) for el in input("Enter values of M,N,K and L separated by space: ").split()]
matrix_inp = [[int(el) for el in input("Enter "+str(values[1])+" consecutive values for row "+str(ind+1)+" of matrix A separate by space: ").split()] for ind in range(0, values[0])]

print("\n".join([" ".join(str(el) for el in row) for row in removeRowCol(matrix = matrix_inp, m=values[0], n=values[1], k= values[2], l=values[3])]))

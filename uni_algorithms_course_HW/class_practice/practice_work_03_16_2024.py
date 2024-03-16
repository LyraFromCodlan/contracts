import heap_sort
import merge_sort
import simple_sorts

from random import randint

# Функция принимает в себя массив на печать и название функции с алгоритмом сортировки
def printResult(array, sort_func):
    print("Исходный массив:")
    print(*array,)

    array = sort_func(array)

    print("Результат:")
    print(*array, end="\n\n")
    
    
# Начала выполнения скрипта
length = int(input("Enter length of an array: "))


# список хранящий названия всех функций, которые могут быть приняты в функцию printResults
sort_functions=[
    simple_sorts.runBubbleSort, 
    simple_sorts.runSelectionSort,
    simple_sorts.runInsertSort,
    simple_sorts.runReverseInsertSort,
    simple_sorts.runQuickSort,
    heap_sort.runHeapSort,
    merge_sort.runMergeSort
]
for func in sort_functions:
    values = [randint(10,99) for ind in range(0,length)]
    printResult(values.copy(), func)
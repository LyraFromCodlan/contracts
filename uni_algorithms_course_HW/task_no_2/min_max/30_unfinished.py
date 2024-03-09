# Дано целое число N и набор из N целых чисел. Найти минимальное количество подряд идущих максимальных элементов из данного набора. 

N = int(input("Enter N value: "))
values = [int(el) for el in input("Enter array of "+str(N)+" values separated by space: ").split()]

maximum = values[0]
min_lenght = N
cur_lenght = 0
left_pointer = 0
right_pointer = 0

while right_pointer<N:
    left_pointer = right_pointer
    if maximum < values[right_pointer]:
        min_lenght = N
        maximum = values[right_pointer]
    if maximum==values[right_pointer]:
        while right_pointer<N:
            if maximum==values[right_pointer]:
                right_pointer+=1
                if right_pointer==N-1:
                    cur_lenght = right_pointer-left_pointer+1
                    if cur_lenght < min_lenght and cur_lenght!=0:
                        min_lenght = cur_lenght
            else:
                if maximum < values[right_pointer]:
                    min_lenght = N
                    maximum = values[right_pointer]
                cur_lenght = right_pointer-left_pointer+1
                if cur_lenght < min_lenght and cur_lenght!=0:
                    min_lenght = cur_lenght
                break

    right_pointer+=1

cur_lenght = right_pointer-left_pointer+1
if cur_lenght < min_lenght and cur_lenght!=0:
    min_lenght = cur_lenght
print(min_lenght)
print(maximum)
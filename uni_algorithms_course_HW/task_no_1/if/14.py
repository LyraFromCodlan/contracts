# If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел. 

numbers = [float(el) for el in input("Enter 3 numbers separated by space: ").split()]
max_num = numbers[0]
min_num = numbers[0]

if max_num>=numbers[1]:
    min_num = numbers[1]
else:
    max_num = numbers[1]

if max_num > numbers[2]:
    if min_num > numbers[2]:
        min_num = numbers[2]
else:
    max_num = numbers[2]

print("max number: "+str(max_num))
print("min number: "+str(min_num))
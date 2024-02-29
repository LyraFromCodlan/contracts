# While30. Даны положительные числа A, B, C. На прямоугольнике размера A × B размещено максимально возможное количество квадратов со стороной C (без наложений). Найти количество квадратов, размещенных на прямоугольнике. Операции умножения и деления не использовать. 

a = int(input("Enter A value: "))
b = int(input("Enter B value: "))
c = int(input("Enter C value: "))

height = 0
width = 0

result = 0

while height+c<=a:
    width = 0
    while width+c<=b:
        result = result+1
        width = width + c
    height = height + c

print("Number of square with size C that fit into AxB square: "+str(result))
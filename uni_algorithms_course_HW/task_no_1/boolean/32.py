# Boolean32°. Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника. Проверить истинность высказывания: «Треугольник со сторонами a, b, c является прямоугольным». 
sides = [float(el)**2 for el in input("Enter length of triangle's sides separated by space: ").split()]


print(sides[0]==sides[1]+sides[2] or sides[1]==sides[0]+sides[2] or sides[2]==sides[1]+sides[0])
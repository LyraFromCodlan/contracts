# Boolean29°. Даны числа x, y, x1, y1, x2, y2. Проверить истинность высказывания: «Точка с координатами (x, y) лежит внутри прямоугольника, левая верхняя вершина которого имеет координаты (x1, y1), правая нижняя — (x2, y2), а стороны параллельны координатным осям».

point = [float(el) for el in input("Enter cooriantes of a point in question in form (X,Y) separated by space: ").split()]
left_top_point = [float(el) for el in input("Enter cooriantes of a top left point in form (X,Y) separated by space: ").split()]
right_bottom_point = [float(el) for el in input("Enter cooriantes of a right bottom point in form (X,Y) separated by space: ").split()]

print((left_top_point[1]>=point[1] and right_bottom_point[1]<=point[1]) and (right_bottom_point[0]>=point[0] and left_top_point[0]<=point[0]))
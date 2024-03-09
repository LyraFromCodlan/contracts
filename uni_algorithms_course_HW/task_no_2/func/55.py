# Описать функцию Leng(xA, yA, xB, yB) вещественного типа, находящую длину отрезка AB на плоскости по координатам его концов:
# |AB| = ((xA − xB)2 + (yA − yB)2)1/2
# (xA, yA, xB, yB — вещественные параметры). С помощью этой функции найти длины отрезков AB, AC, AD, если даны координаты точек A, B, C, D. 

def distance(point_1 : list, point_2 : list):
    return ((point_2[1]-point_1[1])**2+(point_2[0]-point_1[0])**2)**(0.5)

point_1 = [0,0]
point_2 = [3, 4]

print(distance(point_1, point_2))
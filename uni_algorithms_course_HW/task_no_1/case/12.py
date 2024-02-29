# Case12. Элементы окружности пронумерованы следующим образом: 1 — радиус R, 2 — диаметр D = 2·R, 3 — длина L = 2·π·R, 4 — площадь круга S = π·R2. Дан номер одного из этих элементов и его значение. Вывести значения остальных элементов данной окружности (в том же порядке). В качестве значения π использовать 3.14. 

parameters = [float(el) for el in input("Enter option and its value separated by space: ").split()]
pi = 3.14

match parameters[0]:
    case 1:
        print(2*parameters[1])
        print(2*pi*parameters[1])
        print(pi*parameters[1]**2)
    case 2:
        print(parameters[1]/2)
        print(pi*parameters[1])
        print(pi*parameters[1]**2/4)   
    case 3:
        print(parameters[1]/2/pi)
        print(parameters[1]/pi)
        print(parameters[1]/4/pi)
    case 4:
        print((parameters[1]/pi)**0.5)
        print((parameters[1]/pi)**0.5*2)
        print(2*pi*(parameters[1]/pi)**0.5)
# If27. Для данного вещественного x найти значение следующей функции f, принимающей значения целого типа:

#  	 	0,	если x < 0,
# f(x)	 = 	1,	если x принадлежит [0, 1), [2, 3), …,
#  	 	−1,	если x принадлежит [1, 2), [3, 4), … .

x = float(input("Enter x value: "))

if x < 0:
    print(0)
else:
    if x%2<1:
        print(1)
    else:
        print(-1)

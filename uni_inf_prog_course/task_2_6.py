points = [int(point) for point in input("Enter 3 pairs (x,y) of points separated by coma: ").split()]

result : int

square_len_1_2 = (points[2]-points[0])**2+(points[3]-points[1])**2
square_len_2_3 = (points[4]-points[2])**2+(points[5]-points[3])**2
square_len_1_3 = (points[4]-points[0])**2+(points[5]-points[1])**2

if (square_len_1_2 == square_len_1_3 == square_len_2_3 == 0):
    result = 0
elif (square_len_1_2 + square_len_1_3 == 0 or square_len_1_2 + square_len_2_3 == 0 or square_len_1_3 + square_len_2_3 == 0):
    result = 1
elif (points[3]-points[1])*(points[4]-points[2]) == (points[5]-points[3])*(points[2]-points[0]):
    result = 2
elif (square_len_1_2 + square_len_1_3 > square_len_2_3 and square_len_1_2+square_len_2_3>square_len_1_3 and square_len_1_3+square_len_2_3>square_len_1_2):
    result = 3
elif square_len_1_2 == square_len_1_3 + square_len_2_3 or square_len_1_3 == square_len_1_2 + square_len_2_3 or square_len_2_3 == square_len_1_3 + square_len_1_2:
    result = 4

print(result)
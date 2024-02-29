# Case11. Локатор ориентирован на одну из сторон света («С» — север, «З» — запад, «Ю» — юг, «В» — восток) и может принимать три цифровые команды поворота: 1 — поворот налево, −1 — поворот направо, 2 — поворот на 180°. Дан символ C — исходная ориентация локатора и целые числа N1 и N2 — две посланные команды. Вывести ориентацию локатора после выполнения этих команд. 
direction = int(input("Enter direction: "))
directions = ["N","W","S","E"]
cur_direction = 0

match direction:
    case 0:
        pass
    case 1:
        cur_direction = (cur_direction + 1)%4       
    case -1:
        cur_direction = (cur_direction - 1)%4 

direction = int(input("Enter direction"))

match direction:
    case 0:
        pass
    case 1:
        cur_direction = (cur_direction + 1)%4       
    case -1:
        cur_direction = (cur_direction - 1)%4 

print(directions[cur_direction])
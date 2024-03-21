from math import cos

values = [float(el) for el in input(
    "Enter 3 values of start of range, end of range and step of going through range separated by space:\n"
    ).split()]

step = values[0]
cur_value = maximum = cos(step)/(step+1)

while step<=values[1]:
    cur_value = cos(step)/(step+1)
    maximum = maximum if maximum >=  cur_value else cur_value
    step+=0.1
    
print(maximum)
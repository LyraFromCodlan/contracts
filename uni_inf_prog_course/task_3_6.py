from math import cos

step = 0
maximum = cos(step)/(step+1)

while step<11:
    maximum = maximum if maximum >= cos(step)/(step+1) else cos(step)/(step+1)
    step+=1
    
print(maximum)
with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    n,m,k = ifile.readline().strip().split()
    matrix = [[]]
    for row in range(int(n)):
        values = [int(el) for el in ifile.readline().strip().split()]
        if row>0:
            matrix.append([])
        if row==0:
            matrix[0].append(values[0])
        for col in range(len(values)):
            if row<1 and col>=1:
                matrix[row].append(matrix[0][col-1]+values[col])
            elif row>=1 and col<1:
                matrix[row].append(matrix[row-1][0]+values[col])
            elif row>=1 and col>=1:
                matrix[row].append(matrix[row-1][col]+matrix[row][col-1]+values[col]-matrix[row-1][col-1])

    for ind in range(int(k)):
        command = [int(el)-1 for el in ifile.readline().strip().split()]
        x_1,y_1,x_2,y_2=command[0],command[1],command[2],command[3]
        if x_1 == 0 and y_1!=0:
            ofile.write(str(matrix[command[2]][command[3]]-matrix[command[2]][command[1]-1])+"\n")
        elif y_1== 0 and x_1!=0:
            ofile.write(str(matrix[command[2]][command[3]]-matrix[command[0]-1][command[3]])+"\n")
        elif x_1==0 and y_1==0:
            ofile.write(str(matrix[command[2]][command[3]])+"\n")
        else:
            ofile.write(str(matrix[command[2]][command[3]]+matrix[command[0]-1][command[1]-1]-matrix[command[0]-1][command[3]]-matrix[command[2]][command[1]-1])+"\n")
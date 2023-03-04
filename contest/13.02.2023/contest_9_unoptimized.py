with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    n,m,k = ifile.readline().strip().split()
    matrix = []
    pre_sum = [[]]
    for row in range(int(n)):
        matrix.append([int(el) for el in ifile.readline().strip().split()])
    pre_sum[0].append(matrix[0][0])

    for row in range(int(n)):
        if row>0:
            pre_sum.append([])
        for col in range(int(m)):
            if row<1 and col>=1:
                pre_sum[row].append(pre_sum[0][col-1]+matrix[row][col])
            elif row>=1 and col<1:
                pre_sum[row].append(pre_sum[row-1][0]+matrix[row][col])
            elif row>=1 and col>=1:
                pre_sum[row].append(pre_sum[row-1][col]+pre_sum[row][col-1]+matrix[row][col]-pre_sum[row-1][col-1])

    for ind in range(int(k)):
        command = [int(el)-1 for el in ifile.readline().strip().split()]
        x_1,y_1,x_2,y_2=command[0],command[1],command[2],command[3]
        ofile.write(str('')+"\n")
        if x_1 == 0 and y_1!=0:
            print(pre_sum[x_2][y_2]-pre_sum[x_2][y_1-1])
        elif y_1== 0 and x_1!=0:
            print(pre_sum[x_2][y_2]-pre_sum[x_1-1][y_2])
        elif x_1==0 and y_1==0:
            print(pre_sum[x_2][y_2])
        else:
            print(pre_sum[x_2][y_2]+pre_sum[x_1-1][y_1-1]-pre_sum[x_1-1][y_2]-pre_sum[x_2][y_1-1])
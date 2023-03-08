with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    n = int(ifile.readline())
    result = [[1,None],[0,1]]
    for value in range(2,n+1):
        min_ops = result[value-1][0]+1
        prev = value-1
        # if value%2==0:
        #     min_ops = min(min_ops,result[value//2][0]+1)
        # if value%3==0:
        #     min_ops = min(min_ops,result[value//3][0]+1)
        if value%2==0:
            if min_ops>result[value//2][0]+1:
                pass
                min_ops, prev = result[value//2][0]+1, value//2
        if value%3==0:
            if min_ops>result[value//3][0]+1:
                min_ops, prev = result[value//3][0]+1, value//3
        result.append([min_ops, prev])
    ofile.write(str(result[n][0])+'\n')

    operations = [n]
    i = n
    while i > 1:
        operations.append(result[i][1])
        i = result[i][1]
    ofile.write(' ' .join([str(el) for el in operations[::-1]])+'\n')
with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    n = int(ifile.readline())
    result = [2,4,7]
    for ind in range(3,n):
        result.append(result[ind-3]+result[ind-2]+result[ind-1])
    ofile.write(str(result[n-1]))
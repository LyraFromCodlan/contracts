with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    n, k = ifile.readline().split()
    n, k = int(n), int(k)
    result : list = [1]
    for ind in range(k):
        result.append(sum(result))
    for ind in range(k+1,n):
        result.append(sum(result[ind-k:]))
    ofile.write(str(result[n-1]))
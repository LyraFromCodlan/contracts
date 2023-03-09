with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    # n = int(ifile.readline())
    # positions = map(int, ifile.readline().split())
    # positions = sorted(positions)
    # lenght = 0
    # for ind in range(1,len(positions)-1):
    #     if positions[ind]-positions[ind-1]>positions[ind+1]-positions[ind]:
    #         print(str(ind)+": 1")
    #         lenght=lenght+positions[ind+1]-positions[ind]
    #     else:
    #         print(str(ind)+": 2")
    #         lenght=lenght+positions[ind]-positions[ind-1]
    # print(lenght)
    # # print([el for el in positions])

    n = int(ifile.readline())
    lst = [int(i) for i in ifile.readline().split()]
    lst.sort()
    d = [0] * n
    d[1] = lst[1] - lst[0]
    if n > 2:
        d[2] = lst[2] - lst[0]
        for i in range(3, n):
            d[i] = min(d[i - 2], d[i - 1]) + lst[i] - lst[i - 1]
    ofile.write(str(d[n - 1])+'\n')
with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    space = int(ifile.readline().strip())
    os_num = int(ifile.readline().strip())
    os_list = [[],[]]

    for ind in range(0,os_num):
        os = [int(coordinate) for coordinate in ifile.readline().strip().split()]
        if os_list[0]==[]:
            os_list[0].append(os[0])
            os_list[1].append(os[1])
        else:
            i = 0
            while i < len(os_list[0]):
                if os_list[1][i]>=os[0] and os_list[1][i]<=os[1] or os_list[0][i]>=os[0] and os_list[0][i]<=os[1] or os_list[0][i]<=os[0] and os_list[1][i]>=os[1]:
                    os_list[0].pop(i)
                    os_list[1].pop(i)
                else:
                    i+=1
            os_list[0].append(os[0])
            os_list[1].append(os[1])
    ofile.write(str(len(os_list[0]))+"\n")
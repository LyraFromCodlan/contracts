with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    towns_num = int(ifile.readline().strip())
    towns = [int(van) for van in ifile.readline().strip().split()][:20000]
    stack = list()
    new_town_reverse = []

    ind_l = len(towns)-1
    while ind_l>=0:
        ind_r : int = ind_l + 1
        least = True
        while ind_r<len(towns):
            if towns[ind_r]<towns[ind_l] and least:
                least = False
                # print("IND_L = %d; IND_R = %d" % (ind_l, ind_r))
                new_town_reverse.append(str(ind_r))
            ind_r += 1
        if least:
            new_town_reverse.append('-1')
        ind_l -= 1

    ofile.write(' '.join(new_town_reverse[::-1]))

    # print(towns_num)
    # print(towns)
    # print(new_town_reverse[::-1])
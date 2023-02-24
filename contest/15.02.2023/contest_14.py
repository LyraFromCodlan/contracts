with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    van_num = int(ifile.readline().strip())
    vans = [int(van) for van in ifile.readline().strip().split()]

    start = 1
    end = 1
    ind = 0
    while ind < len(vans):
        if vans[ind]==start:
            start = vans[ind]+1
            vans.pop(ind)
            if ind!=0:
                ind-=1
        else:
            ind+=1
    if vans == []:
        ofile.write("YES\n")
    else:
        ofile.write("NO\n")
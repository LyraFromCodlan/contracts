with open("input.txt","r") as ifile, open("output.txt", "r") as ofile:
    # N = int(ifile.readline().strip())
    # for ind in range(N):
    #     iline = ifile.readline().strip()
    #     oline = ofile.readline().strip()
    #     if iline!=oline:
    #         print("Fail on N: %d\niline: %s\noline: %s" % (ind,iline,oline))
    
    iline = [int(el) for el in ifile.readline().strip().split()]
    oline = [int(el) for el in ofile.readline().strip().split()]

    print(len(iline))
    print(len(oline))
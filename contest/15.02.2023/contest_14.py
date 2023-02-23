with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    van_num = int(ifile.readline().strip())
    vans_line_1 = [int(van) for van in ifile.readline().strip().split()]
    vans_line_2 = list()

    print("number of vans: ",str(van_num),";\nvans:",str(vans_line_1))

    stack = list()
    start_van = 1
    ind = 0
    while ind < len(vans_line_1):
        if vans_line_1[ind] == start_van:
            stack = vans_line_1[:ind+1]
            vans_line_1 = vans_line_1[ind+1:]
            stack_ind = 0
            while stack_ind < len(stack):
                if stack[stack_ind] == start_van+1:
                    stack_ind += 1
                # else:
                #     vans_line_2.append[:stack_ind]
        ind+=1
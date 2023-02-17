with open("input.txt","r") as ifile:
    k = int(ifile.readline())
    line = ifile.readline().strip()
    length = len(line)
    max=1

    for ind in range(0,length):
        limit = k
        temp_ind=ind+1
        while temp_ind<length-1:
            if line[temp_ind]!=line[ind]:
                limit-=1
            if limit<0:
                break
            temp_ind+=1
        if max<temp_ind-ind+1:
            max = temp_ind-ind
    print(max)
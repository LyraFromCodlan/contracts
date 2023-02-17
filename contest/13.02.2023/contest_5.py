with open("input.txt","r") as ifile:
    degree_of_beauty : int = 0
    letters_nums=list()
    beauty_degree=0
    n = int(ifile.readline())
    for i in range(0,n):
        letters_nums.append(int(ifile.readline()))

    for ind in range(1,len(letters_nums)):
        if letters_nums[ind]>letters_nums[ind-1]:
            beauty_degree+=letters_nums[ind-1]
        else:
            beauty_degree+=letters_nums[ind]
    print(beauty_degree)
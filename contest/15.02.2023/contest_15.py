with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    towns_num = int(ifile.readline().strip())
    towns = [int(van) for van in ifile.readline().strip().split()]
    stack = list()
    string = []

    ind = len(towns)-1
    while ind>=0:
        print(towns[ind])
        ind -= 1
                

    print(towns_num)
    print(towns)
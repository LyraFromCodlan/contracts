with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    first_player = [int(el) for el in ifile.readline().strip().split()]
    second_player = [int(el) for el in ifile.readline().strip().split()]
    
    ind=0
    while ind<10**6 and (first_player and second_player):
        if (first_player[0]>second_player[0] and not (first_player[0]==9 and second_player[0]==0)) or (first_player[0]==0 and second_player[0]==9):
            first_player.append(first_player[0])
            first_player.append(second_player[0])
            first_player.pop(0)
            second_player.pop(0)
        elif (first_player[0]<second_player[0] and not (first_player[0]==0 and second_player[0]==9)) or (first_player[0]==9 and second_player[0]==0):
            second_player.append(first_player[0])
            second_player.append(second_player[0])
            first_player.pop(0)
            second_player.pop(0)
        ind += 1
    if ind==10**(6):
        ofile.write("botva\n")
    else:
        ofile.write("first %d" % ind if first_player else "second %d" % ind)
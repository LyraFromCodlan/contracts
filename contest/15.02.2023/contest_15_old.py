# this solution uses linked list with double while, hence in worst situation provides TC O(n^2)
# Doesn't pass TC test after 100000 elements in worst case scenarios

with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    towns_num = int(ifile.readline().strip())
    towns = [int(van) for van in ifile.readline().strip().split()]
    stack = list()
    new_town_reverse = []
    min_el = int(towns[-1])

    ind_l = len(towns)-1
    while ind_l>=0:
        if towns[ind_l]<=min_el:
            min_el = towns[ind_l]
            new_town_reverse.append('-1')
        else:
            ind_r : int = ind_l + 1
            least = True    
            while ind_r<len(towns) and least:
                if towns[ind_r]<towns[ind_l] and least:
                    least = False
                    new_town_reverse.append(str(ind_r))
                ind_r += 1
            if least:
                new_town_reverse.append('-1')
        ind_l -= 1

    ofile.write(' '.join(new_town_reverse[::-1]))
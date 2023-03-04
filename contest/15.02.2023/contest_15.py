with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    towns_num = int(ifile.readline().strip())
    towns = [int(van) for van in ifile.readline().strip().split()]
    stack = [[0,towns[0]]]
            
    for ind in range(1,towns_num):
        if towns[ind]>=stack[-1][1]:
            stack.append([ind,towns[ind]])
        else:
            ind_r=len(stack)-1
            while ind_r>=0 and stack[ind_r][1]>towns[ind]:
                towns[stack[ind_r][0]] = str(ind)
                stack.pop()
                ind_r -= 1
            stack.append([ind,towns[ind]])
    
    for el in stack:
        towns[el[0]]="-1"

    ofile.write(' '.join(towns)+'\n')
import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul
}

with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    equation : list =[el for el in ifile.readline().strip().split()]
    ind : int = 0
    while ind <len(equation):
        if equation[ind] in ['+','-','*']:
            equation[ind-2] = ops[equation[ind]](int(equation[ind-1]),int(equation[ind-2]))
            ind -=2
            equation.pop(ind+1)
            equation.pop(ind+1)
        ind += 1
    ofile.write(str(equation)[1:-1]+"\n")
    
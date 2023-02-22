import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul
}

with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    equation : list =[el for el in ifile.readline().strip().split()]
    stack = list()
    ind : int = 0
    while ind <len(equation):
        if equation[ind] in ['+','-','*']:
            if len(stack)==1 and equation[ind]=='-':
                result = 0-stack[-1]
                stack[-1]=result
            else:
                result = ops[equation[ind]](stack[-2],stack[-1])
                stack.pop(-1)
                stack[-1]=result
        else:
            stack.append(int(equation[ind]))
        ind += 1
    ofile.write(str(stack[0])+"\n")
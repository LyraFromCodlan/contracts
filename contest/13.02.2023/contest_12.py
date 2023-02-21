with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    line = ifile.readline()
    stack = list()
    try:
        for ind in range(0,len(line)):
            if line[ind]=='(':
                stack.append('(')
            if line[ind]=='[':
                stack.append('[')
            if line[ind]=='{':
                stack.append('{')
            if line[ind]==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    raise Exception
            if line[ind]==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    raise Exception
            if line[ind]=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    raise Exception
        if stack!=[]:
            raise Exception
        else:
            ofile.write("yes")
    except Exception as e:
        ofile.write("no")
with open('input.txt') as ifile:
    result:str=""
    s: list = [*ifile.readline()]
    stack = []
    while s:
        for el in s:
            if stack==[] or el>stack[-1]:
                stack.append(el)
                s.remove(el)
        result+=''.join(stack)
        stack.clear()
        s.reverse()
    print(result)
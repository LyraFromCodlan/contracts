class Stack:
    stack : list

    def __init__(self) -> None:
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        return "ok\n"

    def pop(self):
        value = str(self.stack[-1])+"\n" if self.stack!=[] else "error\n"
        self.stack = self.stack[:-1]
        return value

    def back(self):
        return str(self.stack[-1])+"\n" if self.stack!=[] else "error\n"

    def size(self):
        return str(len(self.stack))+"\n"

    def clear(self):
        self.stack.clear()
        return "ok\n"

    def exit(self):
        raise Exception


with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    try:
        stack = Stack()
        while True:
            command = ifile.readline().strip()
            if 'push' in command:
                ofile.write(stack.push(int(command.split()[1])))
            if command=='pop':
                ofile.write(stack.pop())
            if command=='back':
                ofile.write(stack.back())
            if command=='size':
                ofile.write(stack.size())
            if command=='clear':
                ofile.write(stack.clear())
            if command=='exit':
                stack.exit()
    except Exception as exception:
        ofile.write("bye")
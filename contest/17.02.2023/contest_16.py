class Queue:
    queue : list

    def __init__(self) -> None:
        self.queue = []

    def push(self, n):
        self.queue.append(n)
        return "ok\n"

    def pop(self):
        value = str(self.queue[0])+"\n" if self.queue!=[] else "error\n"
        self.queue = self.queue[1:]
        return value

    def front(self):
        return str(self.queue[0])+"\n" if self.queue!=[] else "error\n"

    def size(self):
        return str(len(self.queue))+"\n"

    def clear(self):
        self.queue.clear()
        return "ok\n"

    def exit(self):
        raise Exception


with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    try:
        queue = Queue()
        while True:
            command = ifile.readline().strip()
            if 'push' in command:
                ofile.write(queue.push(int(command.split()[1])))
            if command=='pop':
                ofile.write(queue.pop())
            if command=='front':
                ofile.write(queue.front())
            if command=='size':
                ofile.write(queue.size())
            if command=='clear':
                ofile.write(queue.clear())
            if command=='exit':
                queue.exit()
    except Exception as exception:
        ofile.write("bye")
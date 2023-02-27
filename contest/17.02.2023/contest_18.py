class Dequeue:
    dequeue : list

    def __init__(self) -> None:
        self.dequeue = []

    def push_front(self, n):
        self.dequeue.insert(0,n)
        return "ok\n"

    def push_back(self, n):
        self.dequeue.append(n)
        return "ok\n"

    def pop_front(self):
        value = str(self.dequeue[0])+"\n" if self.dequeue!=[] else "error\n"
        self.dequeue = self.dequeue[1:]
        return value

    def pop_back(self):
        value = str(self.dequeue[-1])+"\n" if self.dequeue!=[] else "error\n"
        self.dequeue = self.dequeue[:-1]
        return value

    def front(self):
        return str(self.dequeue[0])+"\n" if self.dequeue!=[] else "error\n"

    def back(self):
        return str(self.dequeue[-1])+"\n" if self.dequeue!=[] else "error\n"

    def size(self):
        return str(len(self.dequeue))+"\n"

    def clear(self):
        self.dequeue.clear()
        return "ok\n"

    def exit(self):
        raise Exception


with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    try:
        dequeue = Dequeue()
        while True:
            command = ifile.readline().strip()
            if 'push_front' in command:
                ofile.write(dequeue.push_front(int(command.split()[1])))
            if 'push_back' in command:
                ofile.write(dequeue.push_back(int(command.split()[1])))
            if command=='pop_front':
                ofile.write(dequeue.pop_front())
            if command=='pop_back':
                ofile.write(dequeue.pop_back())
            if command=='front':
                ofile.write(dequeue.front())
            if command=='back':
                ofile.write(dequeue.back())
            if command=='size':
                ofile.write(dequeue.size())
            if command=='clear':
                ofile.write(dequeue.clear())
            if command=='exit':
                dequeue.exit()
    except Exception as exception:
        ofile.write("bye")
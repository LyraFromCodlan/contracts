class Node:

    def __init__(self, parent) -> None:
        self.value = None
        self.left = None
        self.right = None
        self.parent = parent

class Heap:
    node : Node


    def __init__(self) -> None:
        self.node = Node(None)

    def insert(self, value):
        iterator = self.node
        while iterator != None:
            parent = iterator
            print(parent.value)
            if iterator.left!=None and iterator.right!=None:
                iterator = iterator.left if iterator.right.value>iterator.left.value else iterator.right
            elif iterator.left!=None:
                iterator = iterator.right
            else:
                iterator = iterator.left
        iterator = Node(parent)
        iterator.value = value
        print("Node value: %d" % iterator.value)
        print("Parent value: "+str(parent.value))

lis = [1, 3, 5, 7]
heap= Heap()
heap.insert(lis[0])
heap.insert(lis[1])
heap.insert(lis[2])
heap.insert(lis[3])


# with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
#     command_num = int(ifile.readline().strip())
#     heap = Heap()
#     for ind in range(command_num):
#         command = [int(el) for el in ifile.readline().strip().split()]
#         if command[0]==0:
#             ofile.write(heap.insert(command[1]))
#         elif command[0]==1:
#             ofile.write(heap.extract())

#         print(command)
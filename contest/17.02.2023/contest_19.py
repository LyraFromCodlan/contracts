with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    command_num = int(ifile.readline().strip())
    heap : list = list()
    for ind in range(command_num):
        command = [int(el) for el in ifile.readline().strip().split()]
        if command[0]==0:
            mid = len(heap) // 2
            low = 0
            high = len(heap) - 1
            while low < high:
                if command[1] > heap[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                mid = (low + high) // 2
            if mid>len(heap)-1:
                heap.append(command[1])
            elif mid<0:
                heap.insert(0,command[1])
            else:
                value_ind = mid if heap[mid]>=command[1] else mid+1
                if value_ind>len(heap)-1:
                    heap.append(command[1])
                else:
                    heap.insert(value_ind,command[1])
        elif command[0]==1:
            head = heap[-1]
            ofile.write(str(head)+'\n')
            heap.pop()
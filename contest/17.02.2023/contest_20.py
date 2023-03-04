def heapify(sort_nums, heap_size, root):  
    l = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and sort_nums[left] > sort_nums[l]:
        l = left
    if right < heap_size and sort_nums[right] > sort_nums[l]:
        l = right
    if l != root:
        sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
        heapify(sort_nums, heap_size, l)
def heap(sort_nums):  
    size = len(sort_nums)
    for i in range(size, -1, -1):
        heapify(sort_nums, size, i)
    for i in range(size - 1, 0, -1):
        sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
        heapify(sort_nums, i, 0)

with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    towns_num = int(ifile.readline().strip())
    towns = [int(van) for van in ifile.readline().strip().split()]
    heap(towns)
    ofile.write(' '.join(str(x) for x in towns)+'\n')
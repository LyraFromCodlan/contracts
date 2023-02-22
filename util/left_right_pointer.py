letter : str = input()
limit : int = int(input())
line : str = input().strip()

max_len = 0
right_pointer : int = 0

for left_pointer in range(0,len(line)):
    #cycle
    while limit>=0 and right_pointer<len(line)-1:
        if line[right_pointer]!=letter:
            limit -= 1
        right_pointer += 1
    print("limit = %d; left pointer %s : %d; right pointer %s : %d" % (limit, line[left_pointer], left_pointer, line[right_pointer], right_pointer))
    print("max = %d" % max_len)
    #cycle
    if right_pointer - left_pointer > max_len:
        max_len = right_pointer - left_pointer

    if line[left_pointer]!=letter:
        limit += 1
    
print(max_len)
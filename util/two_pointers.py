limit = int(input())
line = input()
max_len = 0
friquency = dict()
left_pointer = 0

for right_pointer in range(len(line)):
    if line[right_pointer] not in friquency:
        friquency[line[right_pointer]]=0
    friquency[line[right_pointer]] += 1

    length = right_pointer - left_pointer + 1

    if length - max(friquency.values())<=limit:
        max_len = max(max_len, length)
    else:
        friquency[line[left_pointer]] -= 1
        if not friquency[line[left_pointer]]:
            friquency.pop(line[left_pointer])
        left_pointer += 1

print(max_len)
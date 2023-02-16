line: str
container = dict()

with open('input.txt') as ifile:
    for line in ifile:
        for el in line.replace(' ','').replace('\n',''):
            if el not in container.keys():
                container[el]=1
            else:
                container[el]=container[el]+1
maximum = max(container.values())
indexes = ''.join(sorted(container.keys()))
for level in range(0,maximum):
    for ind in indexes:
        if container[ind]<maximum-level:
            print(' ',end='')
        else:
            print('#',end='')
    print()
    if level==maximum-1:
        print(indexes)
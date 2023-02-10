def sort(array:list, indexes: list):
    ind = 1
    while ind!=len(array):
        if abs(array[ind-1]-X)>abs(array[ind]-X) and ind>0:
            array[ind-1],array[ind] = array[ind],array[ind-1]
            indexes[ind-1],indexes[ind] = indexes[ind],indexes[ind-1]

            ind = ind -1
            continue
        ind=ind+1

n = [int(el) for el in input().split()]
N,X,T = n[0],n[1],n[2]
sculptures = [int(el) for el in input().split()]
sculptures_indexes = [int(i) for i in range(1,N+1)]
sort(sculptures, sculptures_indexes)
for ind,scl in enumerate(sculptures):
    T = T - abs(scl-X)
    if T < 0:
        sculptures=sculptures[0:ind]
        sculptures_indexes=sculptures_indexes[0:ind]


if len(sculptures)!=None:
    print(len(sculptures))
    print(' '.join(map(str,sculptures_indexes)))
else: 
    print(sculptures)
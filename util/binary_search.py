k = int(input())
el_list= sorted({int(el) for el in input().split()})

mid = len(el_list) // 2
low = 0
high = len(el_list) - 1

if k<=el_list[0]:
    print("counter=",0)
elif k>el_list[-1]:
    print("counter=",len(el_list))
else:
    while low < high:
        if k > el_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    print("counter=", mid if el_list[mid]>=k else mid+1)  

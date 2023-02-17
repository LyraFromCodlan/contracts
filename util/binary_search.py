k = int(input())
el_list= [int(el) for el in input().split()]

mid = len(el_list) // 2
low = 0
high = len(el_list) - 1
 
while el_list[mid] != k and low <= high and len(el_list[low:high])>=2:
    if k > el_list[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
print(el_list[low:mid+1])
print("ID = ",mid)
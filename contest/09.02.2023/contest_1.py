n = int(input())
reservoir = [int(res) for res in input().split()]

flag = True
for ind in range(0,len(reservoir)-1):
	if reservoir[ind]>reservoir[ind+1]:
		flag=False

print(reservoir[n-1]-reservoir[0] if flag else -1)
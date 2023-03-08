N =10**4
result=[1]

for ind in range(2,10000):
    result.append(ind*result[-1])
result=[result[-1]]
# print(result)
for ind in range(10001,100000):
     result.append(ind*result[-1])

print(result[-1])
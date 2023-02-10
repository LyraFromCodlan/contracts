n = int(input())

def recur(n:int)->int:
    if n in (1,2):
        return n
    else:
         return 2*recur(n-1)-1

print(recur(n)) 
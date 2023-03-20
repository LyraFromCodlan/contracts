# computes ackermann function

def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1,1)
    elif m > 0 and n > 0:
        return ackermann(m-1,ackermann(m,n-1))

with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    m,n = map(int, ifile.readline().strip().split())
    result=str(ackermann(m,n))
    ofile.write(result+'\n')
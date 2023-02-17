import random
import string

N=int(input())

with open("contest_5.txt","w+") as ifile:
    ifile.write(str(N)+"\n")
    for key in range(0,N):
        ifile.write(str(random.randint(0,100))+"\n")
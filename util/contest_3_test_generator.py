import random

with open("contest_3_test.txt","w") as ofile:
    N = random.randint(0,100000)
    diego_stickers = [random.randint(0,1000000000) for ind in range(0,N)]
    K = random.randint(0,100000)
    k_stickers = [random.randint(0,1000000000) for ind in range(0,K)]

    ofile.write(str(N)+"\n")
    ofile.write(' '.join([str(el) for el in diego_stickers])+"\n")
    ofile.write(str(K)+"\n")
    ofile.write(' '.join([str(el) for el in k_stickers])+"\n")
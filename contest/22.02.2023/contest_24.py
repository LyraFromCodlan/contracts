with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    n = int(ifile.readline())
    price_1 = [0] * 5001
    price_2 = [0] * 5001
    price_3 = [0] * 5001
    
    for i in range(1,n+1):
        price_1[i], price_2[i], price_3[i] = map(int, ifile.readline().split())
    time = [0] * (n+1)
    time[0] = 0
    time[1] = price_1[1]
    if n > 1 : time[2] = min(price_1[1] + price_1[2], price_2[1])
    
    for i in range(3, n+1):
        time[i] = min(time[i-1] + price_1[i], time[i-2] + price_2[i-1], time[i-3] + price_3[i-2])
    ofile.write(str(time[-1])+'\n')
with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    n = int(ifile.readline())
    diego_stickers = sorted({int(el) for el in ifile.readline().split()})
    k = int(ifile.readline())
    k_stickers = [int(el) for el in ifile.readline().split()]

    if n == 0:
        if k>0:
            ofile.write("%d\n" % ("0\n"*k)[:-1])
    else:
        for min_sticker in k_stickers:
            if min_sticker<=diego_stickers[0]:
                ofile.write("%d\n" % 0)
            elif min_sticker>diego_stickers[-1]:
                ofile.write("%d\n" % len(diego_stickers))
            else:
                mid = len(diego_stickers) // 2
                low = 0
                high = len(diego_stickers) - 1
                while low < high:
                    if min_sticker > diego_stickers[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                    mid = (low + high) // 2
                ofile.write("%d\n" % (mid if diego_stickers[mid]>=min_sticker else mid+1))
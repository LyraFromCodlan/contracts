# with open("input.txt","r") as ifile:
#     n = int(ifile.readline())
#     diego_stickers = sorted({int(el) for el in ifile.readline().split()})
#     k = int(ifile.readline())
#     k_stickers = [int(el) for el in ifile.readline().split()]

#     if n == 0:
#         if k>0:
#             print(("0\n"*k)[:-1])
#     else:
#         for min_sticker in k_stickers:
#             if min_sticker<diego_stickers[0]:
#                 print(0)
#             elif min_sticker>diego_stickers[-1]:
#                 print(len(diego_stickers))
#             else:
#                 for ind,sticker in enumerate(diego_stickers):
#                     if sticker>=min_sticker:
#                         print(ind)
#                         break

with open("input.txt","r") as ifile:
    n = int(ifile.readline())
    diego_stickers = sorted({int(el) for el in ifile.readline().split()})
    k = int(ifile.readline())
    k_stickers = [int(el) for el in ifile.readline().split()]

    if n == 0:
        if k>0:
            print(("0\n"*k)[:-1])
    else:
        for min_sticker in k_stickers:
            if min_sticker<diego_stickers[0]:
                print(0)
            elif min_sticker>diego_stickers[-1]:
                print(len(diego_stickers))
            else:
                mid = len(diego_stickers) // 2
                low = 0
                high = len(diego_stickers) - 1
                while diego_stickers[mid] != min_sticker and low <= high and len(diego_stickers[low:high])>2:
                    if k > diego_stickers[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                    mid = (low + high) // 2
                print(diego_stickers[low:mid+1])
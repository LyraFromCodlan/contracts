with open("input.txt","r") as ifile:
    n = int(ifile.readline())
    diego_stickers = sorted([int(el) for el in ifile.readline().split()])
    
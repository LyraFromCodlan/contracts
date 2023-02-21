with open("input.txt","r") as ifile, open("output.txt", "w") as ofile:
    line = ifile.readline().strip()
    letters = {el: 0 for el in {char for char in line}}
    for ind in range(len(line)):
        letters[line[ind]] += (ind+1)*(len(line)-ind)
    for key, val in sorted(letters.items()):
        ofile.write(str(key)+": "+str(val)+"\n")
# Text20. Дан текстовый файл. Заменить в нем все подряд идущие пробелы на один пробел. 

lines = []

with open("sample_no_2.txt", "r") as file:
    lines = file.readlines()

for ind in range(0,len(lines)):
    lines[ind] = lines[ind].split()

with open("sample_no_2.txt", "w") as file:
    file.writelines([" ".join(line)+"\n" for line in lines])
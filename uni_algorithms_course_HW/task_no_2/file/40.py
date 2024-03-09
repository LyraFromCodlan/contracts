# File40. Дан файл целых чисел. Заменить в нем каждый элемент с четным номером на два нуля. 
lines = []
with open("sample_no_1.txt", "r") as file:
    lines = file.readlines()
    for line_ind in range(0,len(lines)):
        numbers = [num for num in lines[line_ind].strip().split(" ")]
        for ind in range(0,len(numbers)):
            if float(numbers[ind])%2==0:
                numbers[ind]="00"
        lines[line_ind] = " ".join(numbers)+"\n"
with open("sample_no_1.txt", "w") as file:
    file.writelines(lines)
        

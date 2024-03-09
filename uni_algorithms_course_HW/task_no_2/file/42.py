# File42. Даны два файла произвольного типа. Поменять местами их содержимое. 
lines_1 = []
lines_2 = []
with open("sample_no_2.txt", "r") as file_no_1, open("sample_no_3.txt", "r") as file_no_2:
    lines_1 = file_no_1.readlines()
    lines_2 = file_no_2.readlines()

with open("sample_no_2.txt", "w") as file_no_1, open("sample_no_3.txt", "w") as file_no_2:
    file_no_1.writelines(lines_2)
    file_no_2.writelines(lines_1)

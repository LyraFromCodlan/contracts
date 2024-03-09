# Дана строка, содержащая полное имя файла, т. е. имя диска, список каталогов (путь), собственно имя и расширение. Выделить из этой строки имя файла (без расширения). 

file_path = input("Enter file path: ")
ind = len(file_path)-1
dot_ind = 0
slash_ind = 0
while ind>0:
    if file_path[ind]==".":
        dot_ind = ind
    if file_path[ind]=="\\":
        slash_ind = ind+1
        break
    ind-=1
print(file_path[slash_ind:dot_ind])

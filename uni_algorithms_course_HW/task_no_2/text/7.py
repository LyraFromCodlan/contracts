# Text7. Дана строка S и текстовый файл. Добавить строку S в начало файла.

line = input("Enter new line: ")+"\n" 
lines = []
with open("sample_no_1.txt", "r") as file:
    lines = file.readlines()
with open("sample_no_1.txt", "w") as file:
    file.write(line)
    file.writelines(lines)

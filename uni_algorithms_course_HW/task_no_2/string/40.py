# # String40. Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку, расположенную между первым и последним пробелом исходной строки. Если строка содержит только один пробел, то вывести пустую строку. 

# # # short solution
# # strings = [string for string in input("Enter string containing at least one space:\n").split()]
# # print(" ".join(strings[1:-1]))

# # long solution
string = input("Enter string containing at least one space:\n")
length = len(string)
first_space = True
first_space_ind = 0
last_space_ind = 0
last_space = True
ind = 0
while ind<length and (first_space or last_space):
    if string[ind]==" " and first_space:
        first_space = False
        first_space_ind = ind
    if string[length - ind-1]==" " and last_space:
        last_space = False
        last_space_ind = length-ind-1
    ind+=1
for ind in range(first_space_ind,last_space_ind):
    if string[ind]!=" ":        
        print(string[ind],end="")
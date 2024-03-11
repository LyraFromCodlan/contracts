# Описать функцию PosLast(S0, S) целого типа, возвращающую номер позиции, начиная с которой в строке S содержится последнее вхождение подстроки S0. Если в строке S отсутствуют подстроки S0, то функция возвращает 0. Вывести значения этой функции для пяти данных пар строк S0 и S. 

def posLast(string : str, sub_string: str):
    string_lenght = len(string) 
    sub_string_lenght = len(sub_string)
    ind = string_lenght-1
    while ind > string_lenght-string_lenght:
        if string[ind] == sub_string[sub_string_lenght-1]:
            sub_ind = 0
            while sub_ind < sub_string_lenght:
                if string[ind] == sub_string[sub_string_lenght-1-sub_ind]:
                    if sub_ind == sub_string_lenght-1:
                        return ind
                    ind-=1
                    sub_ind+=1
                else:
                    ind-=1
                    break
        ind-=1
    return 0

string_input = input("Enter string: ")
sub_string_input = input("Enter susbtring last entry of which must be found: ")
print(posLast(string=string_input, sub_string=sub_string_input))
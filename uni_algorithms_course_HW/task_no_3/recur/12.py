# Recur12. Описать рекурсивную функцию DigitCount(S) целого типа, которая находит количество цифр в строке S, не используя оператор цикла. С помощью этой функции найти количество цифр в каждой из пяти данных строк.

# function ord() is used to get ascii of char 
def countDigits(string : str):
    if len(string) == 0:
        return 0
    elif 47 < ord(string[0]) < 58:
        return countDigits(string[1:])+1
    else:
        return countDigits(string[1:])

with open("string_sample_task_12.txt","r") as file:
    string_samples = file.readlines()
    print(
        " ".join(
            [
                str(
                    countDigits(
                        returnValues
                        .strip()
                    )
                )
                for returnValues in string_samples
            ]
        )
    )
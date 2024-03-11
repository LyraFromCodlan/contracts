# Recur13. Описать рекурсивную функцию Palindrome(S) логического типа, возвращающую True, если строка S является палиндромом (т. е. читается одинаково слева направо и справа налево), и False в противном случае. Оператор цикла в теле функции не использовать. Вывести значения функции Palindrome для пяти данных строк.

def checkIfPalindrome(string: str):
    if len(string)==0 or string[0] == string[-1]:
        if len(string)>1:
            return checkIfPalindrome(string[1:-1])
        return True
    else:
        return False

with open("string_sample_task_13.txt","r") as file:
    string_samples = file.readlines()
    print(
        " ".join(
            [
                str(
                    checkIfPalindrome(
                        returnValues
                        .strip()
                        .replace(" ","")
                        .upper()
                    )
                )
                for returnValues in string_samples
            ]
        )
    )
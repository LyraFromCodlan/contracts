for num in range(100,1000,1):
    digits = [int(el)**3 for el in str(num)]
    if num == digits[0] + digits[1] + digits[2]:
        print(num)
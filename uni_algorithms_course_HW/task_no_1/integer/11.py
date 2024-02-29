# Integer11°. Дано трехзначное число. Найти сумму и произведение его цифр. 
digits = [int(el) for el in input()]
digits_sum = 0 
digits_mult = 1
for el in digits:
    digits_mult=digits_mult*el
    digits_sum=digits_sum+el

print("Sum of digits: "+str(digits_sum))
print("Product of digits: "+str(digits_mult))
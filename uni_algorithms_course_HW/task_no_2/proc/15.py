# Описать процедуру ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг: значение A переходит в C, значение C — в B, значение B — в A (A, B, C — вещественные параметры, являющиеся одновременно входными и выходными). С помощью этой процедуры выполнить левый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def shiftLeftByThree(values: list):
    length = len(values)
    values = [values[(ind-2)%length] for ind in range(0,length)]
    return values

sample_no_1 = [1,2,3]
sample_no_2 = [4,5,6]

print(shiftLeftByThree(sample_no_1))
print(shiftLeftByThree(sample_no_2))
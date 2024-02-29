# Begin40°. Найти решение системы линейных уравнений вида

# A1·x + B1·y = C1,
# A2·x + B2·y = C2,

# заданной своими коэффициентами A1, B1, C1, A2, B2, C2, если известно, что данная система имеет единственное решение. Воспользоваться формулами

# x = (C1·B2 − C2·B1)/D,        y = (A1·C2 − A2·C1)/D,
# где D = A1·B2 − A2·B1.


fisrt_coefs = [float(el) for el in input("Enter coefficients of 1st equation of type A*x+B*y=C separated by space: ").split()]
seonds_coefs = [float(el) for el in input("Enter coefficients of 2nd equation of type A*x+B*y=C separated by space: ").split()]

d = fisrt_coefs[0] * seonds_coefs[1] - fisrt_coefs[1]* seonds_coefs[0]
x = (fisrt_coefs[2] * seonds_coefs[1] - fisrt_coefs[1] * seonds_coefs[2])/d
y = (fisrt_coefs[0] * seonds_coefs[2] - fisrt_coefs[2] * seonds_coefs[0])/d

print("x = "+str(x))
print("y = "+str(y))
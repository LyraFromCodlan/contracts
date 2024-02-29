# Begin38°. Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0). 

coefs = [float(el) for el in input("Enter coefficients of 1st equation of type A*x+B=0 separated by space: ").split()]

print("x = "+str(-coefs[1]/coefs[0]))

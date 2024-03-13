values = [float(el) for el in input("Enter 2 values for the function separated by space: ").split()]
s = values[0]
t = values[1]

def h(x, y):
    return (x/(1+y**2))+(y/(1+x**2))-(x-y)**3

def get_max_value(x,y):
    return x if x>=y else y

result = h(s,t)+get_max_value(h(s-t,s*t)**2,h(s-t,s+t)**4)+h(1,1)
print(result)
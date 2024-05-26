
# # a = "🖕"
# # for i in range(12, 50):
# #     for j in range(i):
# #         print(a)
# #     print()
# import numpy as np
# a = np.arange(3)
# print(sum(a*2))
a = 0
b = 1
n = 10000

def f(x):
    return 4/(1 + x**2)

def trapesmetoden(a, b, n):
    summen = 0
    dx = (b - a)/n
    
    for i in range(1, n):
        summen = summen + f(a + i*dx)
    trapessummen = dx/2*(2*summen + f(a) + f(b))
    return trapessummen

print(round(trapesmetoden(a, b, n), 4))
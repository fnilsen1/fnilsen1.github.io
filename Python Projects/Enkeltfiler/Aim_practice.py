import numpy as np
start = 0
slutt = 1
intervaller = 1000
steglengde = (slutt-start)/intervaller
x = np.linspace(start, slutt, intervaller+1)


sum=0

def f(k):
    return np.sqrt(1+1/((1+k**2)**2))

for i in range(1, intervaller+1):

    sum+=steglengde*((f(x[i])+f(x[i-1]))/2)

print(sum)

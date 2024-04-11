import matplotlib.pyplot as plt 
import numpy as np 

x = 1+1j
for i in range(1000):
    x = np.log(x)
print(x)

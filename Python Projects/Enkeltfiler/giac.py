import numpy as np
import matplotlib.pyplot as plt



def giac(n, t):

    sum = 0
    for i in range(n):
        sum+=4/(np.pi*(2*i+1)**2)*np.cos((2*i+1)*t)
    return np.pi/2+sum


x_array = np.linspace(-10, 10, 200)
y_array = giac(1000, x_array)

plt.plot(x_array, y_array)
plt.show()
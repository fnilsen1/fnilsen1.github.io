from pylab import *
import matplotlib.pyplot as plt

m = 200
k = 100
u = 200
v_0 = 0

t = np.linspace(0, 15, 1000)
t1 = np.linspace(15, 30, 1000)

def v1(t):
    c = -(u/k) + v_0
    return (u/k) + c*exp(-(k*t)/m)


def v2(t):
    c = v1(15)
    return c*exp(-(k*t)/m)

plt.plot(t, v1(t))
plt.plot(t1, v2(t))
plt.xlabel("t [s]")
plt.ylabel("Hastighet [m/s]")
plt.grid()
plt.show()



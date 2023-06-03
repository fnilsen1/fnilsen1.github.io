# from pylab import *

# m = 0.05
# F = 1
# B = 0.15
# L = 0.2
# R = 0.025


# def a(v):
#     aks = F/m-((B**2)*(L**2)*v)/(R*m)

#     return aks

# s = 0
# v = 0.001
# t = 0

# s_verdier = [s]
# v_verdier = [v]
# t_verdier = [t]

# dt = 0.001

# while t<=10:
#     v = v + a(v)*dt
#     s = s + v*dt
#     t = t + dt

#     v_verdier.append(v)
#     s_verdier.append(s)
#     t_verdier.append(t)

# figure("Figur 1")
# plot(t_verdier, v_verdier)
# xlabel("$t$ / (s)")
# ylabel("$v$ / (m/s)")
# title("Fart lederstykke")
# grid()

# show()

from pylab import *

m = 0.05
F = 1
B = 0.15
L = 0.2
R = 0.025


def a(v):
    aks = F/m-((B**2)*(L**2)*v)/(R*m)

    return aks

s = 0
v = 0
t = 0
e = 0
p = 0

s_verdier = [s]
v_verdier = [v]
t_verdier = [t]
e_verdier = [e]
p_verdier = [p]


dt = 0.001

while t<=1000:
    v = v + a(v)*dt
    s = s + v*dt
    t = t + dt
    e = v*B*L
    p = (e**2)/R

    v_verdier.append(v)
    s_verdier.append(s)
    t_verdier.append(t)
    p_verdier.append(p)

figure("Figur 1")
plot(t_verdier, s_verdier)
xlabel("$t$ / (s)")
ylabel("$s$ / (m)")
title("Posisjon lederstykke")
grid()


figure("Figur 2")
plot(t_verdier, v_verdier)
xlabel("$t$ / (s)")
ylabel("$v$ / (m/s)")
title("Fart lederstykke")
grid()

figure("Figur 3")
plot(v_verdier, p_verdier)
xlabel("$v$ / (m/s)")
ylabel("$P$ / (w)")
title("Elektrisk effekt")
grid()


show()
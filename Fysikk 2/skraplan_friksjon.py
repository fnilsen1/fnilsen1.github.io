from pylab import *


# Konstanter 

m = 0.400				# massen av gjenstanden, kg

theta = radians(30)	# vinkel for skråplanet

my = 0.35		# friksjonstall

g = 9.81				# tyngdeakselerasjon, m/s^2

# Konstante krefter 

Gx = m*g*sin(theta)	# tyngdekraft langs skråplanet, N

Gy = m*g*cos(theta)	# tyngdekraft normalt på skråplanet, N

N = Gy					# normalkraft på gjenstanden, N
# k=3.22*(10**-3)
# Variable krefter, utregning av kraftsum og akselerasjon 

def a(v):
    # L = -sign(v)*k*v**2
    R = -sign(v)*my*N	# friksjonskraft, motsatt retning av fart

    sum_F = -Gx + R 		# kraftsum, N

    aks = sum_F/m		# akselerasjon, m/s

    return aks

# Startverdier 

s = 0					# startposisjon, m

v = 8.3		# startfart, m/s

t = 0					# starttid, s

# Lister for lagring av data 

s_verdier = [s]

v_verdier = [v]

t_verdier = [t]

# Simulering av bevegelse 

dt = 0.001				# tidssteg i simulering, s

 
while t <= 2:			# krav for stopp av simulering

    v = v + a(v)*dt		# regner ut ny fart

    s = s + v*dt		# regner ut ny posisjon

    t = t + dt			# går til neste tidspunkt


    # Lagring av verdier 

    v_verdier.append(v)
    s_verdier.append(s)
    t_verdier.append(t)

print(s)

# Tegning av graf 

plot(t_verdier, s_verdier)			# lager grafen

xlabel("$t$ / s")					# x-akse-tittel

ylabel("$v$ / (m/s)")				# y-akse-tittel

title("Fartsgraf langs skråplan")	# tittel på grafen

grid()								# legger til rutenett

show()								# viser grafen
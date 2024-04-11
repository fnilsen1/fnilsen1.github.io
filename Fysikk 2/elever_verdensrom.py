from pylab import *

 

# Konstanter 

m = 60					# massen av hver elev, kg

gamma = 6.67*10**(-11)	# gravitasjonskonstanten, Nm^2/kg^2

 

# Variable krefter, utregning av kraftsum og akselerasjon 

def a(r):

	G = gamma*m**2/r**2	# gravitasjonskraft for hver elev, N

	sum_F = G			# kraftsum for hver elev, N

	aks = sum_F/m		# akselerasjon for hver elev, m/s^2

	return aks

 

# Startverdier for bevegelsen 

r1 = 0			# elev 1 starter i origo

v1 = 0			# elev 1 starter i ro

r2 = 1.0		# elev 2 starter 1,0 m fra origo

v2 = 0			# elev 2 starter i ro

r = r2 - r1	# avstanden mellom elevene

t = 0			# starttid

 

# Simulering av bevegelsen 

dt = 0.01				# tidssteg i simuleringen, s

while r > 0:			# stopper simuleringen når elevene møtes

	v1 = v1 + a(r)*dt	# regner ut neste fart for elev 1

	v2 = v2 - a(r)*dt	# regner ut neste fart for elev 2

	r1 = r1 + v1*dt		# regner ut neste posisjon for elev 1

	r2 = r2 + v2*dt		# regner ut neste posisjon for elev 2

	r = r2 - r1			# ny avstand mellom elevene

	t = t + dt			# går til neste tidspunkt

 

print("Tid før kollisjon:", t/3600, "h")
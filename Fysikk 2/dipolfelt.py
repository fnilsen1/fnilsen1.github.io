from pylab import *

 

# Konstanter 

q1 = 2.00e-9			# ladning til kule 1, C

P1 = array([-0.05, 0])	# posisjon til kule 1, m

q2 = -2.00e-9			# ladning til kule 2, C

P2 = array([0.05, 0])	# posisjon til kule 2, m

k = 8.99e9				# konstanten i coulombs lov

 

# Funksjon som beregner det elektriske feltet i posisjonen r 

def E_felt(r):

	r1 = r - P1						# vektor fra P1 til r

	r1_enhet = r1/norm(r1)			# enhetsvektor ut fra P1

	E1 = k*q1/norm(r1)**2 *r1_enhet	# elektrisk felt fra kule 1

	r2 = r - P2						# vektor fra P2 til r

	r2_enhet = r2/norm(r2)			# enhetsvektor ut fra P2

	E2 = k*q2/norm(r2)**2 *r2_enhet	# elektrisk felt fra kule 2

	E = E1 + E2						# summerer feltene fra kulene

	return E						# returnerer det samlede feltet

 

# Beregning 

punkt = array([0, 0.10])	# punktet der vi beregner feltet

E = E_felt(punkt)			# beregning av felt

 

# Vi skriver ut resultatet 

print("Det elektriske feltet i punktet", punkt, "er", E, ".")

print("Det har en absoluttverdi på", norm(E), "V/m.")

print("Vinkelen mellom feltretningen og x⁠-⁠aksen er", arctan(E[1]/E[0]), "radianer.")
# Konstanter 

m = 6.64e-27	# massen av alfapartikkelen, kg

q1 = 3.20e-19	# ladningen til alfapartikkelen, C

q2 = 1.26e-17	# ladningen til gullkjernen, C

k = 8.99e9		# konstant i coulombs lov

 

# Startverdier 

r = -1.0e-10	# startavstand fra kjernen, m

v = 1.5e7		# startfart, m/s

t = 0			# starttid, s

 

# Simulering av bevegelsen 

dt = 1.0e-22	# tidssteg, s

 

while v > 0:	# gjenta så lenge farten er positiv

	a = -k*q1*q2/(m*r**2)	# beregning av akselerasjon, m/s^2

	v = v + a*dt			# beregning av ny fart

	r = r + v*dt			# beregning av ny posisjon

	t = t + dt				# beregning av ny tid

 

print("Alfapartikkelen snur når r =", r, "m")
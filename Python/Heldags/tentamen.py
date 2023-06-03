from pylab import *
# Konstanter
m = 0.050 # massen til lederstykket, kg
L = 0.20 # lengden til lederstykket, m
B = 2 # magnetfelt, T
R = 0.05 # resistans, ohm
F = 9.81 # konstant drakraft, N
# Startverdier og tidssteg
s = 0 # posisjon, m
v = 0 # fart, m/s
t = 0 # tid, s
dt = 0.0001 # tidssted, s
# Lister som lagerer verdier
s_liste = [s] # liste med verdier for posisjon

v_liste = [v] # liste med verdier for fart
t_liste = [t] # liste med verdier for tid
# Funksjon som regner ut og returnerer akselerasjon
def a(v):
 F_el = v*L**2*B**2/R # regner ut elektrisk kraft, N

 if(s>=0.2):
    F_sum = F - F_el # kraftsum, N
 else:
    F_sum = F
 aks = F_sum/m

 return aks
# Løkke som beregner nye verdier
while s <= 0.6: 
 
 v = v + a(v)*dt # regner ut ny fart
 s = s + v*dt # regner ut ny posisjon
 t = t + dt # regner ut ny tid
 s_liste.append(s) # legger posisjon i liste
 v_liste.append(v) # legger fart i liste
 t_liste.append(t) # legger tid i liste

print(t) #Hvor lang tid det tar før den er helt inne i magnetfeltet

# Plotter bevegelse
plot(t_liste, s_liste) # lager plot
xlabel("$t$/s") # tekst på x-akse
ylabel("$s$/m") # tekst på y-akse
title("Strekning som funksjon av tid") # tittel på graf
grid() # viser rutene
show() 


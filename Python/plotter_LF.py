#Redigeringslogg:
#2023 - Emil Johnsen
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tikzplotlib import save as save_tikz
#Husk at dere må ha disse pakkene installert. Dette kan gjøres med pip

# Vi bruker denne for å få pyplot til å bruke latex til tegning av figurtekst på akser osv
# Det går også an å sette fontstørrelse her, men å sette figurstørrelsen vil i de fleste tilfeller
# ha samme effekt
# Hvis dere ikke ønkser å bruke latex til tegning av figurtekst på akser osv, må dere kommentere ut de følgende kodelinjene
plt.rcParams.update({
   "text.usetex": True,
   "font.family": "sans-serif",
   "font.sans-serif": ["Helvetica"]})

# Her kan dere legge inn flere filer om dere trenger det
file1 = "csv-fil som inneholder data dere ønsker å plotte"

data1 = pd.read_csv(file1)

# Hent ut måleserie og tid, konverter til numpy
time = data1.iloc[:,0].to_numpy()
signal = data1.iloc[:,1].to_numpy()

time = time - np.min(time) # Setter starten på tidsaksen til 0
time = time*1000 # Setter tidsakse til ms

# Plot med pyplot, her kan dere bruke så mye avanserte funksjoner dere vil, med subplots osv
fig,a = plt.subplots(1,1)
# Vi hopper 100 punkter om gangen her for å spare regnekraft når vi tegner plottet. Denne må tilpasses til hvor tett data er samplet
a.plot(time[::100],signal[::100])
a.set_xlabel("$t$ [ms]")
a.set_ylabel("$V$ [V]")

# Lagre data i et egnet format, her ligger eksempler for både tikz og eps
# Dersom du bruker Tikz, må du bruke pakkene pgfplots og tikz i latex-dokumentet ditt
# Enkel lagring
save_tikz('filsti.../filNavn.tex') #Merk: denne funker ikke om dere bruker plt.show() i scriptet
# Mer avansert, her legger vi inn symboler for å styre figurstørrelsen som vi kan styre
# direkte i latex
save_tikz('filsti.../filNavn.tex',axis_height='\\figH',axis_width='\\figW') #Merk: denne funker ikke om dere bruker plt.show() i scriptet

# Bruker du sistnevnte, må du legge til følgende 4 linjer i latex-dokumentet ditt:
# \newlength\figH
# \newlength\figW
# \setlength{\figH}{4cm}
# \setlength{\figW}{8cm}

# For eps må du bruke pakken graphicx i latex
# Med eps lagres plottet som et bilde, som betyr at
# dere må justere størrelsen på figuren manuelt før dere lagrer for å sikre at fontstørrelsen
# blir lesbar:
fig.set_size_inches(4,3)
plt.tight_layout()
plt.savefig('filNavn.eps',format='eps')

# Viser plottet til slutt for å sjekke om alt ser greit ut - MERK: denne må kommenteres ut om dere bruker save_tikz
plt.show()
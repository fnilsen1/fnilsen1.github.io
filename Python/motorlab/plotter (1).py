#Redigeringslogg:
#2023 - Emil Johnsen
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tikzplotlib import save as save_tikz #MERK: dette biblioteket er ikke standard i anaconda, og må installeres

# Vi bruker denne for å få pyplot til å bruke latex til tegning av figurtekst på akser osv
# Det går også an å sette fontstørrelse her, men å sette figurstørrelsen vil i de fleste tilfeller
# ha samme effekt
# Hvis dere ikke ønkser å bruke latex til tegning av figurtekst på akser osv, må dere kommentere ut de følgende kodelinjene
# plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "sans-serif",
#    "font.sans-serif": ["Helvetica"]})
plt.rcParams.update({
   "text.usetex": False,
   "font.family": "sans-serif",
   "font.sans-serif": ["Arial"]})  # Use a sans-serif font available in your TeX distribution


# Her kan dere legge inn flere filer om dere trenger det
file1 = "Hastighetsreferanse_part1_PF.csv"

#leser csv-fila
data1 = pd.read_csv(file1)

# Hent ut måleserie og tid, konverter til numpy
time = data1.iloc[:,0].to_numpy()
signal = data1.iloc[:,1].to_numpy()


# 1) Sett tidsaksen til å starte på 0
# 2) Pass på at tidsaksen er i millisekunder (datapunktene vi henter ut fra filene er i sekunder)
# ----- SKRIV DERES KODE HER -----
time_in_milliseconds = time * 1000  # sec to ms
time_in_milliseconds -= time_in_milliseconds[0] # move start to 0
# --------------------------------

# Plot med pyplot, her kan dere bruke så mye avanserte funksjoner dere vil, med subplots osv
fig, ax = plt.subplots(1,1)

# 1) Fest plot av målt signal mot tid til a - Merk: det er ofte veldig mange datapunkter, så ofte bør man velge ut f.eks. hvert tiende
#    eller hvert hundrende punkt for å spare regnekraft.
# 2) Sett labels på aksene
# ----- SKRIV DERES KODE HER -----
downsample_factor = 1000
downsampled_time = time_in_milliseconds[::downsample_factor]
downsampled_signal = signal[::downsample_factor]

# ax.plot(time_in_milliseconds, signal)
ax.plot(downsampled_time, downsampled_signal)

ax.set_xlabel('Time (ms)')
ax.set_ylabel('Signal Value')
ax.set_ylim(0, 8)
# --------------------------------

# Lagre data i et egnet format, her ligger eksempler for både tikz og eps
# Dersom du bruker Tikz, må du bruke pakkene pgfplots og tikz i latex-dokumentet ditt
# Enkel lagring - Merk: dersom dere ikke ønsker å få ut en tex-figur, kan dere kommentere ut de følgende linjene
# save_tikz('chan2.tex')
# Mer avansert, her legger vi inn symboler for å styre figurstørrelsen som vi kan styre
# direkte i latex
# save_tikz('filNavn.tex',axis_height='\\figH',axis_width='\\figW')

# Bruker du sistnevnte, må du legge til følgende 4 linjer i latex-dokumentet ditt:
# \newlength\figH
# \newlength\figW
# \setlength{\figH}{4cm}
# \setlength{\figW}{8cm}

# For eps må du bruke pakken graphicx i latex
# Med eps lagres plottet som et bilde, som betyr at
# dere må justere størrelsen på figuren manuelt før dere lagrer for å sikre at fontstørrelsen
# blir lesbar: - Merk hvis dere ikke ønsker en figur i esp-format må dere kommentere ut de følgende linjene
fig.set_size_inches(4,3)
plt.tight_layout()
# plt.savefig('figur.eps',format='eps')

# 1) Vis plottet til slutt for å sjekke om alt ser greit ut - Merk: hvis dere bruker save_tiks, må dette kommenteres ut for
#    at dere skal få ut en tex-figur
# ----- SKRIV DERES KODE HER -----
ax.grid(alpha=0.2)
plt.show()
# --------------------------------
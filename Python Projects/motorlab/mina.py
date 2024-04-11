import numpy as np 
import matplotlib.pyplot as plt   
import numpy as np
import matplotlib.pyplot as plt


REF_VOLTAGE = 2.98

DATA = np.genfromtxt('bode_data.xlsx', delimiter=':').transpose()

DATA = DATA[:, DATA[0, :].argsort()]

FREKVENS = DATA[0]
FORSTERKNING = DATA[2] 
FASE_VINKEL = -DATA[1]

forsterkning_db = 20 * np.log10(FORSTERKNING)

fig, (ax1, ax2) = plt.subplots(2)
fig.set_size_inches(7, 10)

ax1.set_xscale("log")
ax1.set_xlabel("Frekvens [Hz]")
ax1.set_ylabel("Forsterkning [dB]")
ax1.plot(FREKVENS, forsterkning_db)

ax2.set_xscale("log")
ax2.set_xlabel("Frekvens [Hz]")
ax2.set_ylabel("Fase forsyvning [°]")
ax2.plot(FREKVENS, FASE_VINKEL)

plt.show()
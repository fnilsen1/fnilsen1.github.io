import csv
import matplotlib.pyplot as plt

filnavn = "Python\Eksamensprep\oppgave11.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser


with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")
  dato = []
  kostnader = []

  for rad in filinnhold:
    if(rad[0][3:5]=="01" or rad[0][3:5]=="02" or rad[0][3:5]=="03"):
        dato.append(rad[0])
        kostnader.append(int(rad[2]))

  plt.figure(figsize=(10, 5))          # Angir dimensjoner for figure-objektet
  plt.barh(dato, kostnader)  # Lager stolpediagrammet
  plt.subplots_adjust(left=0.4)        # Øker plassen på venstre side av diagrammet
  plt.grid(axis="x")                   # Legger til rutenett (bare vertikale linjer)     
  plt.show()  
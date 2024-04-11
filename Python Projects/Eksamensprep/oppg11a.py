import csv
import matplotlib.pyplot as plt

filnavn = "Python\Eksamensprep\oppgave11.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)

  sum = 0
  for rad in filinnhold:
    sum+=int(rad[2])
  print(sum)
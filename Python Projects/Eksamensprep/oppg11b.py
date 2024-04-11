import csv
import matplotlib.pyplot as plt

filnavn = "Python\Eksamensprep\oppgave11.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)

  sum_liste = [0,0,0]

  for rad in filinnhold:
    if(rad[0][3:5]=="01"):
      sum_liste[0]+=int(rad[2])
    
    if(rad[0][3:5]=="02"):
      sum_liste[1]+=int(rad[2])
         
    if(rad[0][3:5]=="03"):
      sum_liste[2]+=int(rad[2])


  print(sum_liste)
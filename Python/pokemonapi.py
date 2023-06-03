import json
import requests as req
import matplotlib.pyplot as plt
import numpy as np
import os

#Innstillinger for programmet
visiblePokemon = 8
availableStats = ["hp", "attack", "defense", "special-attack", "special-defense", "speed"]
shownStat = availableStats[4] 
fileName = "PokemonPie.json"

#main løkken for programmet 
def main():
  while True:
    chosenPokemon = [] #pokemon valgt av brukeren. hver pokemon er satt inn med navn
    url = f"https://pokeapi.co/api/v2/pokemon?limit={visiblePokemon}&offset=0" #url for de aktuelle pokemon

    while len(chosenPokemon)<6: #kjører til 6 pokemon er valgt
      result = req.get(url) # henter informasjonen fra urlen
      data = result.json() #gjør om resultatet til dict, som python kan behandle
      next = data["next"] #neste side, som inneholder de neste n pokemon
      prev = data["previous"] #forrige side, som inneholdte de forrige n pokemon
      selectablePokemon = [[pk["name"],pk["url"]] for pk in data["results"]] #lagrer navnet og urlen til hver pokemon på skjermen
      os.system("clear") #tømmer terminalen
      while True:#valgmenyen
        print(f'''
        ______________________
        |  --Velg Pokemon--  |
        |____________________|''')
        for index, poke in enumerate(selectablePokemon):
          print(f"\t| {index+1} : {poke[0].capitalize():<13}{'* |' if poke[0] in chosenPokemon else '  |'}")#legger til en stjerne hvis pokemonen eksisterer i listen over valgte pokemon
        print(" "+"-"*37)
        print(f"{'a: <-- ' if prev != None else ' '*7} | s: se forrige graf | {'d: -->' if next != None else ''}")
        print("\tENTER : lukk programmet")

        try:#try except for å behandle bruker input
          inputPokemon = input(">")
          validInputs = ["a" if prev != None else ..., "d" if next != None else ..., "", "s"] #alle valide inputs som ikke er nummer.
          if inputPokemon in validInputs or int(inputPokemon) in range(1,visiblePokemon+1): # sjekker om inputtet er i mengden av alle valide inputs
            break
          raise Exception("skriv et tall i mengden") #for når tallet ikke er i mengden
        except ValueError as e:#for når teksten ikke er en gyldig kommando
          print("skriv noe som gir mening")
          input()
        except Exception as e:
          print(e)
          input()
        os.system("clear") #tømmer terminalen

      if inputPokemon == "a":# når inputtet er sjekket for riktig verdi, kan det testes for presis verdi
        url = prev
        continue
      elif inputPokemon == "d":
        url = next
        continue
      elif inputPokemon == "s":
        renderPreviousGraph()
        continue
      elif inputPokemon == "":
        print("lukker programmet...")
        return
      else:#når input er et nummer i mengden:
        pokemonChosen = selectablePokemon[int(inputPokemon)-1][0]
        if pokemonChosen in chosenPokemon:#fjerner pokemon fra valgte pokemon hvis allerede valgt
          chosenPokemon.remove(pokemonChosen)
        else:  #legger til navnet i listen over valgte pokemon
          pokemonChosen = selectablePokemon[int(inputPokemon)-1][0]
          chosenPokemon.append(pokemonChosen)

    info = collectInfo(chosenPokemon,shownStat)#Henter informasjonen om statsene til hver pokemon. Returnerer en liste over tall

    showGraph(chosenPokemon,info,shownStat) #tegner en graf fra all informasjonen sanket


def collectInfo(chosenPokemon:list,shownStat:str):
  """
  Iterates through every pokemon in the chosenPokemonList, and returns a list of the stat values of the chosen stat for each pokemon
  """
  statData = []
  
  for pk in chosenPokemon:
    url = f"https://pokeapi.co/api/v2/pokemon/{pk}" #henter info av her pokemon
    result = req.get(url)
    data = result.json()
    stats = data["stats"]
    for stat in stats: #itererer gjennom hver stat i listen og finner den riktige
      if stat["stat"]["name"] == shownStat:
        statData.append(stat["base_stat"])
        break
    
  newdata = { #skriver dette inn i json filen
    "pokemon":chosenPokemon,
    shownStat:statData
  }
  with open(fileName,"w") as file:
    file.write(json.dumps(newdata,indent=6, sort_keys = True))
  return statData


def renderPreviousGraph():#tegner den forrige grafen med informasjonen lagret i json filen
  """
  Collects the information from the json file, and sends it to the showGraph() function to be displayed
  """
  with open(fileName,"r") as file:
    data = json.load(file)
    keys = []
    for key in data:
    # henter alle keys i json filen. navnene er alltid lagret først, og vil være den første keyen i datasettet. Den andre keyen har et varierende navn, men er alltid nr 2. Henter informasjonen derfor gjennom plassering istedenfor navnet på keyen
      keys.append(key)
      
    showGraph(data[keys[0]],data[keys[1]],keys[0])

def showGraph(chosenPokemon,statData,chosenStat):
  """"
  Displays a graph with the given information from the parameters
  """
  labelForGraph = [f"{pokemon} ({statData[index]})" for index,pokemon in enumerate(chosenPokemon)]
  plt.pie(np.array(statData), labels = labelForGraph)
  plt.title(chosenStat)
  plt.show()

if __name__ == "__main__": #hvorfor ikke
  main()
  
"""
https://pokeapi.co/docs/v2
"""
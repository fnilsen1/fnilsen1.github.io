import json
import matplotlib.pyplot as plt
import requests as req
import numpy as np

"""
Spør om stat_list.stat_list
Filstruktur
Om filen havner på riktig sted
"""

class Variabel:
    def __init__(self):
        self.stat_list = []
stat_obj = Variabel()

stat = "defense"
valgt_liste = []
limit = 5
offset = 0

type_farge = {
    "normal": "#A8A77A",
    "fire": "#EE8130",
    "water": "#6390F0",
    "electric": "#F7D02C",
    "grass": "#7AC74C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#735797",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD"
}

def vis_verdi(verdi):
    return int(np.round(verdi/100.*sum(stat_obj.stat_list), 0))


def vis_liste(offset, limit, valgt_liste):

    while True:
        
        url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
        resultat = req.get(url)
        data = resultat.json()
        print("\nListe over pokemon: ")
        for i in range(len(data["results"])):
            if(data["results"][i]["name"].capitalize() in valgt_liste):
                print(f'\033[1;34;40m{i+1}. {data["results"][i]["name"].capitalize()}\033[0m')
                
                
            
            else:
                print(f'{i+1}. {data["results"][i]["name"].capitalize()}')
        print("""
Handlinger:          
a: forrige
d: neste
e: exit
Velg pokemon ved å skrive nr
        """)

        valg = input("Input handling: ")
        
        try:
            
            if(valg == "a" and offset !=0):
                offset-=limit

            elif(valg == "d"):
                offset+=limit

            elif(valg == "e"):
                print("Du har avsluttet programmet")
                break
                
            
            else: 
                valg = int(valg)
                valgt_pokemon = data["results"][int(valg)-1]["name"].capitalize()
                if(valgt_pokemon in valgt_liste):
                    valgt_liste.remove(valgt_pokemon)
                    print(f'Du har fjernet {valgt_pokemon}')
                    print("Dine valgte er:")
                    print(valgt_liste)

                else:
                    print(f'Du har valgt {valgt_pokemon}')
                    valgt_liste.append(valgt_pokemon)
                    print("Dine valgte er:")
                    print(valgt_liste)
                    

                    if(len(valgt_liste)==6):

                        farger = []
                        
                        for j in range(len(valgt_liste)):

                            lower_case = (valgt_liste[j][0].lower() + valgt_liste[j][1:])

                            url = f"https://pokeapi.co/api/v2/pokemon/{lower_case}"
                            resultat = req.get(url)
                            data = resultat.json()
                            for item in data["stats"]:
                                if(item["stat"]["name"]==stat):
                                    stat_obj.stat_list.append(int(item["base_stat"]))
                            
                            
                            

                            url = f"https://pokeapi.co/api/v2/pokemon/{valgt_liste[j].lower()}"
                            resultat = req.get(url)
                            data = resultat.json()
                            farger.append(type_farge[data["types"][0]["type"]["name"]])


                        plt.pie(stat_obj.stat_list, labels=valgt_liste, colors=farger,autopct=vis_verdi)
                        
                        plt.title(f"{stat.capitalize()} Stats")
                        
                        plt.show()

                        pie_obj = {}
                        for i in range(len(valgt_liste)):
                            pie_obj[valgt_liste[i]]={stat:stat_obj.stat_list[i],"farge":farger[i]}

                        filnavn = "PokemonPie.json"
                        with open(filnavn, "w") as fil:
                            fil.write(json.dumps(pie_obj))
                        
                        valgt_liste=[]
                        stat_obj.stat_list = []
                        print("Listen er tilbakestilt, velg nye")
                        
        except:
            pass

# vis_liste(offset, limit, valgt_liste)  
# obj = {}
# url1 = f"https://pokeapi.co/api/v2/pokemon?limit=1008&offset=0"

# resultat = req.get(url1)
# data1 = resultat.json()
# for i in range(1008):
#     navn = data1["results"][i]["name"]
#     url2 = f"https://pokeapi.co/api/v2/pokemon/{navn}"
#     resultat = req.get(url2)
#     data2 = resultat.json()
#     a=0
#     for item in data2["stats"]:
#         a+=item["base_stat"]
#     obj[navn]=a
# print(obj)

def sort_dict_by_value(dictionary):
    return [key for key, value in sorted(dictionary.items(), key=lambda item: item[1])]

filnavn = "Python/Pokemon/stats.json"

with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)



print(sort_dict_by_value(data))
import json
import sys
import requests as req
from pprint import PrettyPrinter

#Trenger ikke ha url utenfor og inni
#filnavn = ""
valgte_liste = []
limit = 5
offset = 0

pp = PrettyPrinter()

# url = "https://pokeapi.co/api/v2/pokemon/pikachu" #bytt ut med ønsket navn
# url = "https://pokeapi.co/api/v2/ability/battle-armor"
url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}" #alle pokemon med nummer
# url = "https://pokeapi.co/api/v2/pokemon/25/" #gir samme resultat som pikachu over
# url = "https://pokeapi.co/api/v2/pokemon/11/"



# print(f"Statuskode: {resultat.status_code}")





# print(data["results"][0]["name"])


def vis_liste(url, offset, limit):

    while True:
        url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
        resultat = req.get(url)
        data = resultat.json()
        print("\nListe over pokemon: ")
        for i in range(len(data["results"])):
            if(data["results"][i]["name"].capitalize() in valgte_liste):
                print(f'\033[1;34;40m{data["results"][i]["name"].capitalize()}\033[0m')
                
                
            
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
                sys.exit()
            
            else: 
                valg = int(valg)
                valgt_pokemon = data["results"][int(valg)-1]["name"].capitalize()
                if(valgt_pokemon in valgte_liste):
                    valgte_liste.remove(valgt_pokemon)
                    print(f'Du har fjernet {valgt_pokemon}')
                    print("Dine valgte er:")
                    print(valgte_liste)
                else:
                    print(f'Du har valgt {valgt_pokemon}')
                    valgte_liste.append(valgt_pokemon)
                    print("Dine valgte er:")
                    print(valgte_liste)


        except Exception as e:
            # print(e)
            pass




vis_liste(url, offset, limit)



valg = """
Dine valg:
All info
ability
base_experience
height
game_indices
"""

# pp.pprint(data)
# print(data["game_indices"][0]["ability"]["name"])


# for i in range(len(data["game_indices"])):
#     print(data["game_indices"][i]["version"]["name"])



# print(type([])==list)

# brukerinput = (input(valg))

def info(valg):
    if(valg == "ability"):
        print(data["abilities"][0]["ability"]["name"])
    elif(valg == "base_experience"):
        print(data["base_experience"])


    
# info(brukerinput)

# filnavn = "Python/pokemon_test2.txt"

# with open(filnavn, "w") as fil:
#   # fil.write(json.dumps(pp.pprint(data)))
#   fil.write(json.dumps(data, indent=6, sort_keys=True))
  
""" Oppgave
Lek med instillinger og se på json filen for å få litt forståelse.
Link til hvordan denne API-en kan brukes:
https://pokeapi.co/docs/v2

Noen ting dere kan prøve å få til:
Lag et infosystem om pokemon

Dere kan skrive ut en liste over x antall pokemon. Gjerne 5-9 et sted
  Hint: url = "https://pokeapi.co/api/v2/pokemon?limit=2&offset=2" #test denne å se om dere får noen ideer her
  next: inneholder linken til neste antall
  previous: inneholder forrige
  
Listen kan komme opp på denne måten: 
1: navn
2: et annet navn
3: osv
..
n: siste navn i denne listen

Brukeren skal kunne velge et tall her og da skal valgfri info om den pokemonen komme opp. 

Det skal være mulig å komme tilbake til forrige ledd i menyen sånn at du ikke setter deg fast i søket. 

Det skal sikres at brukeren ikke kan skrive feil info ved hjelp av try except.
"""
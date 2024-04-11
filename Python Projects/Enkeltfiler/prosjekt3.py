import json
import requests as req
from pprint import PrettyPrinter
from termcolor import colored
import matplotlib.pyplot as plt
pp=PrettyPrinter

filename="liste.pokemon.json"

def Clear(): #Rydder opp terminalen
    return print(chr(27) + "[2J")

def Get_pokemon(url):#Skaffer json til liste over pokemon
    result_pokemon = req.get(url)
    return result_pokemon.json()

def Get_specficpokemon(url): #Skaffer json til ønsket spessifik pokemon
    result_specificpokemon = req.get(url)
    return result_specificpokemon.json()

def Get_color(id): #Skaffer farge fra url til spessifik pokemon 
    url_color=f"https://pokeapi.co/api/v2/pokemon-color/{id}/"
    url_resultat= req.get(url_color)
    data_color=url_resultat.json()
    data_color=data_color["name"]
    return data_color

def Show(data_pokemon): #Viser frem pokemon 
    bredde=25
    pokemon_valgt=False

    print(f"""
|{"Pokemon:":<{bredde}}
|{"":-^{bredde}}   """)
    for n in range(5):
        url = data_pokemon["results"][n]["url"]
        result = Get_specficpokemon(url)
        try:
            for item in valgte_pokemon:
                if result["name"]==item[0]:
                    pokemon_valgt = True
        except:
            pass
        if pokemon_valgt is True:
            print(colored(f"|{result['id']}:   {data_pokemon['results'][n]['name']}", "green"))
            pokemon_valgt=False
        else:
            print(f"|{result['id']}:   {data_pokemon['results'][n]['name']}")
    print(f'|\n|{"":-^{bredde}}', end="")    
    print(f"\n|z:Next  |x:Previous")
    print("|e:Exit\n")

def Next(data_pokemon): #Viser de neste pokemonene
    url=data_pokemon["next"]
    data_pokemon=Get_pokemon(url)
    return data_pokemon

def Previous(data_pokemon): #Viser de tidligere pokemonene
    url=data_pokemon["previous"]
    data_pokemon=Get_pokemon(url)
    return data_pokemon

def optiontree(data_pokemon):#Lager ett valgtre som sender deg videre eller gir tilbake informasjon ut i fra hva du putter inn
    optiontree=input(";")
    try:
        optiontree=str(optiontree)
        if optiontree=="z":
            data_pokemon=Next(data_pokemon)
            return data_pokemon
        elif optiontree=="x":
            data_pokemon=Previous(data_pokemon)
            return data_pokemon
        elif optiontree=="e":
            data_pokemon=1
            return data_pokemon
    except:
        pass
    # except Exception as ex:
    #     if optiontree not in("z", "x", range(1, 2000)):
    #         print("Du må velge ett av alternativene")
    #         input()
    #         return data_pokemon
    # try:
    #     optiontree=str(optiontree)
    #     if optiontree=="x":
    #         data_pokemon=Previous(data_pokemon)
    #         return data_pokemon

    # except Exception as ex:
    #     print(ex)
    try:
        optiontree=int(optiontree)
        for n in range(5):
            url = data_pokemon["results"][n]["url"]
            result = Get_specficpokemon(url)
            
            if optiontree==result["id"]:
                pokemon_alleredevalgt=False
                try:
                    for n, item in enumerate(valgte_pokemon):
                        if item[0]==result["name"]:
                            pokemon_alleredevalgt=True
                            valgte_pokemon.pop(n)
                            return data_pokemon
                except:
                    pass
                if pokemon_alleredevalgt is False:
                    valgte_pokemon.append([result["name"], url])
                    print("valgte er", len(valgte_pokemon))
                    if len(valgte_pokemon)==6:
                        Values_diagram(data_pokemon)
                    return data_pokemon
            else:
                optiontree_notexisting=True
        if optiontree_notexisting is True:
            print("Du må velge ett av alternativene!!")
            input()
            return data_pokemon
            
        
        return data_pokemon

    except:
        print("Du må velge ett av alternativene!!")
        input()
        return data_pokemon
            
def Make_diagram(names, values, colors):#Lager ett kakediagram
    plt.pie(values, labels=names, colors=colors)
    plt.show()

def Make_file(dict):#Lager fil med informasjon fra kakediagrammet
    with open("PokemonPie.json", "w") as file:
        file.write(json.dumps(dict, indent=6, sort_keys=True))

def Values_diagram(data_pokemon): #Finner fram informasjonen som skal brukes i kakediagrammet
    names_pokemon=[]
    weights_pokemon=[]
    colors_pokemon=[]
    thisdict={}
    for n, pokemon in enumerate(valgte_pokemon):
        url = pokemon[1]
        # url = data_pokemon["results"][n]["url"]
        result = Get_specficpokemon(url)
        color=Get_color(result["id"])
        thisdict[f"{n}"]={
            "name":f"{pokemon[0]}",
            "weight":f"{result['weight']}",
            "color":f"{color}"
        }
        addition=f"{str(result['weight'])}weight"
        names_pokemon.append(pokemon[0]+" "+addition)
        weights_pokemon.append(result['weight'])
        colors_pokemon.append(color)
    Make_diagram(names_pokemon, weights_pokemon, colors_pokemon)
    Make_file(thisdict)
        
data_pokemon = Get_pokemon(f"https://pokeapi.co/api/v2/pokemon?limit=5&offset=0")

valgte_pokemon = []

while data_pokemon!=1:
    Clear()
    Show(data_pokemon)
    data_pokemon=optiontree(data_pokemon)

print("FINISHED")
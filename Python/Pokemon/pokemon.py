#Importerer bibliotek
import json
import matplotlib.pyplot as plt
import requests as req
import numpy as np

#Lager en klasse Variabeloversikt
class Variabeloversikt:
    def __init__(self):
        self.stat = "defense"
        self.limit = 5
        self.offset = 0
        self.stat_list = []
        self.farger = []
        self.valgt_liste = []
        self.data = ""
        self.valg = ""
"""
Lager et objekt med klassen Variabel for å kunne
endre disse verdiene inni alle funksjoner.
Dette er i stedet for å bruke global
"""
obj = Variabeloversikt()

#Dictionary som assosierer pokemon type med en heksadesimal fargekode
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

#Definerer en funksjon kalt main som inneholder alle andre funksjoner
def main():
    #while loop som kjører helt til brukeren går ut av programmet eller breaker loopen
    while True:
        #Kjører funksjon kalt meny. Denne printer listen med pokemon i terminalen
        meny()

        #Tar brukerinput og lagrer det i attributtet valg
        obj.valg = input("Input handling: ")
        
        #Try og except gjør at vi ikke får feilmeldinger når brukeren skriver inn feil.
        #Hvis det skjer en feil, så går den over til except og går fra toppen av while-loopen på nytt
        try:
            #Setter url'en til vårt api-kall
            url = f"https://pokeapi.co/api/v2/pokemon?limit=1&offset=0"
            #Henter ut informasjonen fra json-filen for denne url'en
            resultat = req.get(url)
            #Lagrer informasjonen i dictionaryform i variabelen data
            data = resultat.json()
           
           #Input gjør at du endrer api-kallet og kan bla fram og tilbake
           #obj.offset !=0 gjør at vi ikke kan bla til side -1 f.eks
            if(obj.valg == "a" and obj.offset !=0):
                obj.offset-=obj.limit

            #Passer på at vi ikke kan bla til en side som ikke finnes
            elif(obj.valg == "d" and obj.offset<data["count"]-obj.limit):
                obj.offset+=obj.limit

            #break gjør at vi hopper ut av for-loopen og avslutter programmet
            elif(obj.valg == "e"):
                print("Du har avsluttet programmet")
                break
                
            #Hvis du skriver inn et tall (1-5), så havner du her
            else: 
            #Vi kjører funksjonen oppdater_liste fordi du har valgt en pokemon
                oppdater_liste()

        #Dersom inputen din ikke blir plukket opp av en if, så havner du her.
        #I stedet for å kræsje programmet, så sier vi pass og kjører while-loopen fra start
        except:
            pass

#Definerer en funksjon kalt meny. Denne printer listen med pokemon i terminalen
def meny():
        #Vi har to variabler inni i lenken som endrer api-kallet
        url = f"https://pokeapi.co/api/v2/pokemon?limit={obj.limit}&offset={obj.offset}"
        resultat = req.get(url)
        obj.data = resultat.json()

        #Vi viser valgte pokemon med blå skrift
        print("\nListe over pokemon: ")
        for i in range(len(obj.data["results"])):
            if(obj.data["results"][i]["name"].capitalize() in obj.valgt_liste):
                print(f'\033[1;34;40m{i+1}. {obj.data["results"][i]["name"].capitalize()}\033[0m')
                
                
            #Printer navnene til pokemon vi ikke har valgt i listen
            else:
                print(f'{i+1}. {obj.data["results"][i]["name"].capitalize()}')
        #Printer ut menyen i terminalen
        print("""
Handlinger:          
a: forrige
d: neste
e: exit
Velg pokemon ved å skrive nr
        """)

"""
Definerer funksjonen oppdater_liste som oppdaterer listen over valgte pokemon.
Vi kan enten legge til eller fjerne pokemon.
Dersom lengden på listen blir 6, så viser vi kakediagrammet og lager en json-fil.
Til slutt fjerner vi alt fra listen over valgte pokemon.
"""
def oppdater_liste():
    obj.valg = int(obj.valg)
    valgt_pokemon = obj.data["results"][int(obj.valg)-1]["name"].capitalize()
    if(valgt_pokemon in obj.valgt_liste):
        obj.valgt_liste.remove(valgt_pokemon)
        print(f'Du har fjernet {valgt_pokemon}')
        print("Dine valgte er:")
        print(obj.valgt_liste)

    else:
        print(f'Du har valgt {valgt_pokemon}')
        obj.valgt_liste.append(valgt_pokemon)
        print("Dine valgte er:")
        print(obj.valgt_liste)
        

        if(len(obj.valgt_liste)==6):
            vis_plot()
            pokemon_pie_json()

            obj.valgt_liste=[]
            obj.stat_list = []
            print("Listen er tilbakestilt, velg nye")

#Vi definerer funksjonen vis_plot som viser et kakediagram med en bestemt stat
def vis_plot():             
    obj.farger = []
    for j in range(len(obj.valgt_liste)):

        lower_case = (obj.valgt_liste[j].lower())

        url = f"https://pokeapi.co/api/v2/pokemon/{lower_case}"
        resultat = req.get(url)
        obj.data = resultat.json()
        for item in obj.data["stats"]:
            if(item["stat"]["name"]==obj.stat):
                obj.stat_list.append(int(item["base_stat"]))
    
        url = f"https://pokeapi.co/api/v2/pokemon/{obj.valgt_liste[j].lower()}"
        resultat = req.get(url)
        obj.data = resultat.json()
        obj.farger.append(type_farge[obj.data["types"][0]["type"]["name"]])

    """
    Vi spesifiserer hvilke to lister vi skal bruke for å lage kakediagrammet,
    hvilke farger hver bit skal ha og hvilke verdier som skal vises.
    """
    plt.pie(obj.stat_list, labels=obj.valgt_liste, colors=obj.farger, autopct=vis_verdi)
    
    plt.title(f"{obj.stat.capitalize()} Stats")
    
    plt.show()

"""
Vi definerer en funksjon pokemon_pie_json som først lager en dictionary. 
Denne ordboken erstatter enten innholdet i en eksisterende json-fil kalt "PokemonPie.json",
eller lager en ny fil med dette navnet og innholdet.

"""
def pokemon_pie_json():
    pie_obj = {}
    for i in range(len(obj.valgt_liste)):
        pie_obj[obj.valgt_liste[i]]={obj.stat:obj.stat_list[i],"farge":obj.farger[i]}

    filnavn = "PokemonPie.json"
    with open(filnavn, "w") as fil:
        fil.write(json.dumps(pie_obj, indent=2, sort_keys=True))
    


"""
Funksjon som tar 'verdi' som parameter og gjør f.eks defense stat om til verdier som vises
på pie chart. Det er vanlig å vise % i pie chart, så denne funksjonen regner om og viser
det vi hentet ut fra api-en. 
""" 

def vis_verdi(verdi):
    return int(np.round(verdi/100.*sum(obj.stat_list), 0))

#Kaller på funksjonen main()
if __name__ == "__main__":
    main()  



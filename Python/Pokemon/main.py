from os import system
from requests import get
import matplotlib.pyplot as plt

class Session:
    def __init__(self) -> None:
        self.page, self.chosenPokemon = 0, []
        self.allPokemon = {pokemon["name"]: pokemon["url"] for pokemon in get("https://pokeapi.co/api/v2/pokemon?limit=1279").json()["results"]}
    
    def showPieChart(self) -> None:
        pokemonNames = [str(list(self.allPokemon.keys())[pokemon-1]) for pokemon in self.chosenPokemon]
        pokemonSpeedStats = [get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}").json()["stats"][5]["base_stat"] for pokemonName in pokemonNames]
        pokemonNames = [name.capitalize() for name in pokemonNames]
        
        explode = [0 for _ in range(6)]
        if pokemonSpeedStats.count(max(pokemonSpeedStats)) == 1: explode[pokemonSpeedStats.index(max(pokemonSpeedStats))] = 0.1

        fig, ax1 = plt.subplots()
        ax1.pie(pokemonSpeedStats, explode=explode, labels=pokemonNames, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title("Pie chart of pokemon speed")
        plt.show()
        self.page, self.chosenPokemon = 0, []
    
    def printUI(self) -> None:
        pokemonToShow, pageMovePromt = [], "\"q\": quit  "

        if self.page == 0:
            pokemonToShow = list(self.allPokemon.keys())[:5]
            pageMovePromt += "\"d\": next page"
        elif self.page == 255:
            pokemonToShow = list(self.allPokemon.keys())[1275:]
            pageMovePromt += "\"a\": previous page"
        else:
            pokemonToShow = list(self.allPokemon.keys())[self.page*5:(self.page+1)*5]
            pageMovePromt += "\"d\": next page  \"a\": previous page"
        
        system("clear")
        print(f" --- Page {self.page+1} ---\n")
        for i, pokemon in enumerate(pokemonToShow):
            numb = i+1+self.page*5
            if numb in self.chosenPokemon: print(f"\u001b[36m{numb}. {pokemon.capitalize()}\u001b[0m")
            else: print(f"{numb}: {pokemon.capitalize()}")
        print(f"\nTotal number of currently chosen pokemon: {len(self.chosenPokemon)}\n\n{pageMovePromt}")
    
    def inputNotInRange(self, userChoice) -> bool:
        if not(self.page*5<userChoice<=(self.page+1)*5):
            input("Invalid input\n > ok")
            return True
    
    def userInputIsStr(self, userChoice: str) -> int:
        if userChoice == "a" and self.page != 0:
            self.page -= 1
            return -1
        elif userChoice == "d" and self.page != 255:
            self.page += 1
            return -1
        elif userChoice == "q":
            system("clear")
            return -2
        else:
            input("Invalid input\n > ok")
            return -1
    
    def testUserInput(self, userChoice: str) -> int:
        try:
            """
            Prøver å gjøre om 'userChoice' til et heltall. Om det funker hopper koden over alle 'except'-blokkene.
            """
            return int(userChoice)
        except ValueError:
            """
            Om koden gir 'ValueError' betyr det at den ikke kunne gjøre om 'userChoice' til et heltall.
            Koden sjekker da om brukeren skal til neste eller forrige side, eller om 'userChoice' er ugyldig.
            """
            return self.userInputIsStr(userChoice)
        except Exception as e:
            """
            Om koden gir en annen error enn 'ValueError', har vi lyst til å logge dette.
            Linje 68 kan byttes ut med en mer "proff" logge-metode enn kun print.
            F.eks. logg til en ekstern fil.
            """
            print(f"\n{e}\n")
            raise
    
    def execute(self) -> None:
        while True:
            self.printUI()
            userChoice = self.testUserInput(input(" > "))
            if userChoice == -1: continue
            elif userChoice == -2: break
            elif self.inputNotInRange(userChoice): continue
            elif userChoice in self.chosenPokemon: self.chosenPokemon.pop(self.chosenPokemon.index(userChoice))
            else: self.chosenPokemon.append(userChoice)
            if len(self.chosenPokemon) == 6: self.showPieChart()

if __name__ == "__main__":
    session = Session()
    session.execute()
import requests as req
import matplotlib.pyplot as plt
import json
import matplotlib.pyplot as plt


offset = 0



def showMenu(offset):

    selectedPokemonList = []
    statList = []   
    while True:


        try:
            response = req.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit=5")
            data = response.json()
            print("\nList of Pokemon: ")
            for i in range(len(data["results"])):
                if(data["results"][i]["name"].capitalize() in selectedPokemonList):
               
                    print(f'\033[31m{i+1}. {data["results"][i]["name"].capitalize()}\033[0m')
                
                else:
                    print(f'{i+1}. {data["results"][i]["name"].capitalize()}')
            print("""       
a: last
s: next
exit: exit
or choose a pokemon by number
            """)

            action = input("Input action: ")

            if(action == "a" and offset !=0):
                offset-=5

            elif(action == "s"):
                offset+=5

            elif(action == "exit"):
                break
                
            
            else: 
                action = int(action)
                selectedPokemon = data["results"][int(action)-1]["name"].capitalize()
                if(selectedPokemon in selectedPokemonList):
                    selectedPokemonList.remove(selectedPokemon)
                    print("Selected Pokemon:")
                    print(selectedPokemonList)

                else:
                    print(f'You have chosen {selectedPokemon}')
                    selectedPokemonList.append(selectedPokemon)
                    print("Selected Pokemon:")
                    print(selectedPokemonList)
                    

                    if(len(selectedPokemonList)==6):

               
                        for j in range(len(selectedPokemonList)):

                            lowerCase = (selectedPokemonList[j][0].lower() + selectedPokemonList[j][1:])

                            url = f"https://pokeapi.co/api/v2/pokemon/{lowerCase}"
                            resultat = req.get(url)
                            data = resultat.json()
                            
                            statList.append(data["stats"][0]["base_stat"])

                        

                        plt.pie(statList, labels=selectedPokemonList)
                        
                        plt.title("HP")
                        
                        plt.show()
                        


                        PokemonPie = {}
                        for i in range(len(selectedPokemonList)):
                            PokemonPie[selectedPokemonList[i]]={"hp":statList[i]}

                        
                        with open("PokemonPie.json", "w") as fil:
                            fil.write(json.dumps(PokemonPie, indent=2))
                        
                        selectedPokemonList = []
                        statList = []   
                        print("List is reset")
        except:
            pass

    
showMenu(offset)



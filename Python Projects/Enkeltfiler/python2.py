import requests
url = f"https://www.worldcubeassociation.org/api/v0/competitions/Bartebyen2023/wcif?fbclid=IwAR0JAuHPErKNDH2FXmLFsOF3cgOi4laTNEKhDuYV5rOzjMO0yxivuI_Eras"
response = requests.get(url)
data = response.json()
print(data)
# def get_pokemon_info(pokemon_name):
#     url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         print(f"Name: {data['name']}")
#         print(f"Height: {data['height']} decimetres")
#         print(f"Weight: {data['weight']} hectograms")
#         print("Abilities:")
#         for ability in data['abilities']:
#             print(f"- {ability['ability']['name']}")

# get_pokemon_info("pikachu")
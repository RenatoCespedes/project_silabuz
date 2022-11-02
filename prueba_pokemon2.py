import requests
print("Ejemplos de ID: 25,342,351(tiene forma),352,...")
k=int(input("Ingrese ID del pokemon: "))
pokemon=f'https://pokeapi.co/api/v2/pokemon/{k}'
resp = requests.get(pokemon)
dato=resp.json()
#Formas
url_pokemon=[k['url'] for k in dato['forms']]
name_pokemon=[k['name'] for k in dato['forms']]
resp_form = requests.get(url_pokemon[0])
dato_form = resp_form.json()
lista_formas = [k['language']['name'] for k in dato_form['form_names']]  
#Habitat
resp_habitat = requests.get(dato['location_area_encounters'])
dato_habitat = resp_habitat.json() 
lista_habitat = [k['location_area']['name'] for k in dato_habitat] 
#resultados
print(70*"_")
print("Resultados: ")
print(f"ID: {k}, y nombre del pokemon: {name_pokemon[0]}")
print(f"URL del form-pokemon: {url_pokemon[0]}")
print(f"Lista de formas: {lista_formas}")
print(f"Lista de habitat: {lista_habitat}")
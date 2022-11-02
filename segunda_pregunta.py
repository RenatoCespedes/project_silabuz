import requests
class Pokemon:
    def __init__(self):
        self.nombre=""
        self.generacion=""
        self.formas=""
        self.habilidad=""
        self.habitat=""
        self.tipo=""
print("Cargando datos ... ")
lista_pokemons=[]
#351-356 aleatorios
for k in range(351,356):
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
    a=Pokemon()
    a.nombre=name_pokemon[0]     
    a.formas=lista_formas
    a.habitat=lista_habitat
    lista_pokemons.append(a)   
print("¡Completado¡")
print(" ")
def listar_generacion():
    print("Listar pokemon por generacion")
def listar_forma():
    print("Listar pokemon por forma")
    print('Muestras de formas: ja-Hrkt, ko, zh-Hant, es') 
    forma_in=input("Ingrese una forma: ").lower()
    for v in lista_pokemons:
        if forma_in in v.formas:
            print(f'Nombre del pokemon: {v.nombre}')
def listar_habilidad():
    print("Listar pokemon por habilidad")
def listar_habitat():
    print("Listar pokemon por habitat")
    print("Muestras de habitat: unova-route-6-area, hoenn-route-119-area,... ")
    habit_in=input("Ingrese un habitat: ")
    for n in lista_pokemons:
        if habit_in in n.habitat:
            print(f'Nombre del pokemon: {n.nombre}')
def listar_tipo():
    print("Listar pokemon por tipo")

def menu():
    opciones=True
    while opciones:
        print("MENU")
        print("Opción 1: Listar pokemons por generación")
        print("Opción 2: Listar pokemons por forma")
        print("Opción 3: Listar pokemons por habilidad")
        print("Opción 4: Listar pokemons por habitat")
        print("Opción 5: Listar pokemons por tipo")
        print("Opción 6: Salir")
        opcion=int(input("Digite una opción: "))
        if opcion==1:
            listar_generacion()
        elif opcion==2:
            listar_forma()
        elif opcion==3:
            listar_habilidad()
        elif opcion==4:
            listar_habitat()
        elif opcion==5:
            listar_tipo()
        elif opcion==6:
            opciones=False
        else:
            print("Ingrese de 1 a 6")
menu()

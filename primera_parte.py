import csv
lista_libros=[]
class Libro:
    def __init__(self):
        self.titulo=""
        self.genero=""
        self.id_ISBN=""
        self.editorial=""
        self.autores=""
def leer_archivo():
    print("Leer archivos CSV o txt")
def listar_libros():
    print("Listado de libros")
    for v,a in enumerate(lista_libros):
        print(f"{v} -> {a.titulo}, {a.genero}, {a.id_ISBN}, {a.editorial}, {a.autores}")
def agregar_libro():
    print("Agregar libro")
    print("Ingrese los siguientes datos del libro: ")
    nm=Libro()
    nm.titulo=input("Título del libro: ")
    nm.genero=input("Género del libro: ")
    nm.id_ISBN=input("ID o ISBN: ")
    nm.editorial=input("Editorial: ")
    nmk=int(input("Ingrese la cantidad de autores: "))
    autor=[]
    for vk in range(nmk):
        a=input(f"Ingrese el autor {vk+1}: ")
        autor.append(a)
    nm.autores=autor
    lista_libros.append(nm)
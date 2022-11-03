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
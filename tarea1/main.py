import csv


class Libro:
    def __init__(self):
        self.__archivo=""
        self.__id=0
        self.__titulo=""
        self.__genero=""
        self.__id_ISBN=""
        self.__editorial=""
        self.__autores=[]
        self.lista_libros=[]
    
    #SETTER
    def set_id(self,i):
        self.__id=i
    def set_archivo(self,y):
        self.__archivo=y
    
    def set_titulo(self,tittle):
        self.__titulo=tittle
    def set_genero(self,x):
        self.__genero=x
    def set_isbn(self,code):
        self.__id_ISBN=code
    def set_editorial(self,ed):
        self.__editorial=ed
    def set_autor(self,autor):
        autor=autor.split(',')
        for i in autor:
            self.__autores.append(i)
    def set_attributes(self,id,titulo,genero,isbn,editorial,autores):
        self.__id=id
        self.__titulo=titulo
        self.__genero=genero
        self.__id_ISBN=isbn
        self.__editorial=editorial
        self.__autores=autores
    #GETTER
    def get_attributes(self):
        return self.__id,self.__titulo,self.__genero,self.__id_ISBN,self.__editorial,self.__autores
    
    def get_archivo(self):
        return self.__archivo
    
def leer_archivo(archivo):
    
    with open(archivo) as f:
            # next(f)
        x=csv.reader(f)
        next(x)
        for row in x :
            libro=Libro()
            libro.set_archivo(archivo)
            libro.set_id(row[0])
            libro.set_titulo(row[1])
            libro.set_genero(row[2])
            libro.set_isbn(row[3])
            libro.set_editorial(row[4])
            libro.set_autores(row[5])
            libro.lista_libros.append(libro)


leer_archivo('libro.csv')

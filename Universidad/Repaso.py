# from collections import namedtuple
from random import randint
# # Estructura de datos, coleccion

# # Listas

# listas = [0,1,2,3,4]

# # Vectores no existen en python. Entonces, que son?
# # Los vectores son listas convencionales a las cuales les imponemos un limite de tamaño.

# DIMF = 8
# vector = [0,1,2,3,4,5,6,7,8,9,10]


# if len(vector) < DIMF:
#     vector.append()
# else: 
#     print("Vector lleno")


# # Matrices
# matriz = [[0,0,0],
#           [1,1,1],
#           [2,2,2]]


# # Namedtuples
# autos = namedtuple("autos",["marca","modelo","patente","kilometraje"])

# mi_autito = autos("Mercedez",2016,"AB153DC",50.0)


# # Diccionarios
# diccionarios = {
#     "key":"value",
#     "key":"value",
#     "key":"value",
#     "key":"value",
# }

# persona = {
#     "nombre":"Juan Reynoso",
#     "apodo":"El Crack",
#     "edad":31,
#     "sueldo":float(input("Ingrese su sueldo: "))
# }

# print("Imprimimos todo el diccionario")
# print(persona)

# print("\nImprimimos solo unos pocos datos.")
# print(persona["apodo"])
# mi_autito.patente = "Ford"

# Objetos
# Es una forma de represantar elementos del mundo real.  
# Los procedimientos y funciones pasan a llamarse METODOS.
# Las variables y constantes pasan a llamarse ATRIBUTOS.


class Mamifero:             
    # Es un constructor. Basicamente, se encarga de construir el objeto cuando lo instanciamos.
    def __init__(self,nombre,numero_de_tetas,patas,genero,mensaje=""):         
        self.nombre = nombre
        self.numero_de_tetas = numero_de_tetas
        self.patas = patas
        self.genero = genero
        self.mensaje = mensaje


    def Andar(self):
        if self.patas < 1:
            print("Nadooooo, nadoooooooo")
        else:
            print("Caminoooo, caminooooo")


    def hablar(self):
        print(self.mensaje)    


Perrito = Mamifero("Flopy",7,4,"Re macho","TENGO HAMBRE")
Ballena = Mamifero("Omph",0,0,"Hembra","Ahhhhh")
Humano = Mamifero("Brandon",1,2,"Machito opresor","Soy el rey de la montaña")

# Perrito.hablar()
# Ballena.hablar()
# Humano.hablar()

# Listas Enlazadas por Nodos


class Nodo:
    def __init__(self,elemento,siguiente = None):
        self.elemento = elemento
        self.siguiente = siguiente

class ListaEnlazadaOrdenada:
    def __init__(self):
        self.head = None

    def AgregarOrdenado(self,dato):
        self.nuevo_elemento = Nodo(dato,None)
        self.elemento_actual = self.head
        self.elemento_anterior = self.head

        # Primer elemento = 3
        # dato nuevo = 8 

        #  La cabeza esta vacia O  el nuevo elemento era mas pequeño que el primero.
        if (self.head is None) or (self.nuevo_elemento.elemento <= self.head.elemento):
            self.nuevo_elemento.siguiente = self.head
            self.head = self.nuevo_elemento                                          # El primer elemento es ahora el nuevo elemento.
   
        else:
            while (self.elemento_actual is not None) and (self.nuevo_elemento.elemento >= self.elemento_actual.elemento):
                self.elemento_anterior = self.elemento_actual
                self.elemento_actual = self.elemento_actual.siguiente 

            if not(self.elemento_actual == None):
                self.nuevo_elemento.siguiente = self.elemento_actual
            self.elemento_anterior.siguiente = self.nuevo_elemento


    # Funcion recursiva.
    def __print_recursivo(self,dato):
        if dato != None:                                  # Condicion de corte
            self.__print_recursivo(dato.siguiente)        # Llamada recursiva
            print(dato.elemento,end=" -> ")

    def print_recursivo(self):
        self.__print_recursivo(self.head)


lista = ListaEnlazadaOrdenada()

for i in range(10):
    
    lista.AgregarOrdenado(i)

lista.print_recursivo()
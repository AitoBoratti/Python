"""
A RESOLVER
En un estacionamiento céntrico, un playero realiza el control de ingreso y egreso de autos con la siguiente operatoria:
Se tiene un listado ordenado por patente de vehículos que son habituales. 
(ya está cargado en memoria, la lista debe crearla)


Cada vez que ingresa un vehículo al estacionamiento, se debe verificar si está en la lista.


En caso de no estar registrado se piden los siguientes datos: patente, horas de estadía y conductor, 
generando una lista que se inserta al principio con el nuevo cliente (es una lista los nuevos clientes). 


Una vez ingresado al estacionamiento, se asigna el número de box, registrando el mismo en una lista ordenada 
por patente (lista de estacionamiento), con la cantidad de horas de estadía en cada caso.

Actividades
Desarrollar toda la operatoria del playero. 
Al finalizar los controles se desea recorrer recursivamente el listado y obtener el total de horas de 
estacionamiento de ese día
"""



class Auto:
    def __init__(self, patente, horas_estadia, conductor, box=None):
        self.patente = patente
        self.horas_estadia = horas_estadia
        self.conductor = conductor
        self.box = box


class Nodo:
    def __init__(self,auto,siguiente):
        self.auto = auto
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.head = None


    def verificar_existencia(self,dato):
        dato_actual = self.head
        while (dato_actual.auto.patente != self.head.auto.patente) or (dato_actual == None):
            if (dato_actual.auto.patente == self.head.auto.patente):
                return dato_actual
            dato_actual = dato_actual.siguiente
        return None
    

    def agregar_inicio(self,dato):
        nuevo_nodo = Nodo(dato,None)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo


    def agregar_ordenado(self,dato):
        self.nuevo_elemento = Nodo(dato,None)
        self.elemento_actual = self.head
        self.elemento_anterior = self.head

        if (self.head is None) or (self.nuevo_elemento.auto.patente <= self.head.auto.patente):
            self.nuevo_elemento.siguiente = self.head
            self.head = self.nuevo_elemento                                         
   
        else:
            while ((self.elemento_actual is not None) and 
                   (self.nuevo_elemento.auto.patente >= self.elemento_actual.auto.patente)):
                self.elemento_anterior = self.elemento_actual
                self.elemento_actual = self.elemento_actual.siguiente 

            if not(self.elemento_actual == None):
                self.nuevo_elemento.siguiente = self.elemento_actual
            self.elemento_anterior.siguiente = self.nuevo_elemento


    def _total_horas_recursivo(self,dato):
        total = 0
        if dato is not None:
            self._total_horas_recursivo(dato.siguiente)
            return dato.auto.horas_estadia
        return 0

    def total_horas_recursivo(self):
        return self._total_horas_recursivo(self.head) 


clientes_habituales = ListaEnlazada()
nuevos_clientes = ListaEnlazada()
lista_estacionamiento = ListaEnlazada()
lista_estacionamiento = ListaEnlazada()

alla_clientes = True


while alla_clientes:
    patente = input("Ingrese su patente: ")
    cliente = clientes_habituales.verificar_existencia(patente)


    if cliente == None:
        cliente = Auto(patente=patente,
                        horas_estadia=input("Ingrese las horas de estadia: "),
                        conductor=input("Ingrese su nombre: "))
        nuevos_clientes.agregar_inicio(cliente)


    cliente.box = input("Ingrese un numero de box: ")
    lista_estacionamiento.agregar_ordenado(cliente)


lista_estacionamiento.total_horas_recursivo()


 
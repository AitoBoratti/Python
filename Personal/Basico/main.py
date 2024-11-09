from collections import namedtuple 

# Tupla = Registro inmodificable 

producto = namedtuple("producto",[
    "cod",
    "nombre",
    "proveedor",
    "stock",
    "costo" ])
productos=[] # Lista vacia


nuevoProducto = producto(0,"Aito","dsg",10,100.0)
nuevoProducto2 = producto(1,"Ahito","FSFdsg",100,150.0)

nuevoProducto = nuevoProducto._replace(costo = 0)


print(nuevoProducto)
print(nuevoProducto2)
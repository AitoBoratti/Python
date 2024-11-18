## Operaciones de los tipos de datos.
#  Se prioriza la conservacion de los datos antes que la eficiencia. 
#  
### Tipos de operaciones:
#  Concatenacion: Es basicamente la suma, pero entre strings o chars
#                 La adhicion de texto a un string. Todos los tipos de datos 
#                 tendran valores literales
#  Mapeado, o conversion: En escencai, es forzar un tipo de dato a volverse otro.
#       tipo_de_dato_deseado(dato_a_convertir)
#  
## Operaciones de numeros enteros y flotantes:
    # Numero1 = 5
    # Numero2 = 3
    

    #   Numero1 += Numero2 = 8
        
    #   Numero1 -= Numero2 = 2
        
    #   Numero1 *= Numero2 = 15
        
    #   Numero1 /= Numero2 = 5/3

    #   Numero1 **= Numero2 = 125

    # Numero1 = 10
    # Numero2 = 3
    #   Modulo = Numero1 % Numero 2 == 1

## Operaciones booleanas:
# a == b:  Compara si A es equivalente B, devuelve true en caso de serlo, o false si no.
# a >= b:  Compara si A es mayor a B, devuelve true en caso de serlo, o false si no.
# a <= b:  Compara si A es menor a B, devuelve true en caso de serlo, o false si no.
# a != b:  Compara si A es diferente a B, devuelve true en caso de serlo, o false si no.
#
#Estructoras de control:
#Es la forma de contralar el flujo de un programa.  
#
## El if es la forma mas basica de controlar el flujo de un programa, en caso de cumplir una condicion,
# accedera a ella. En caso de ser falso, se evaluara la siguiente, o se ira al else.
#if (condicion):
#   verdadera.
#
#elif (nueva condicion):
#   segunda condicion verdadera.
# 
# else
#   falsa:
#
## El match (o case) sirve para evaluar condiciones de forma similar al if, pero es usado para evaluar
## el valor de un unico dato que puede tomar muchas opciones ( >4)
#
# print("=== MENÚ PRINCIPAL ===")
# print("1. Ver perfil")
# print("2. Editar perfil")
# print("3. Configuración")
# print("4. Ayuda")
# print("5. Salir")
# print("======================")
# opcion = int(input("Por favor, elige una opción (1-5): "))

# match opcion:
#     case 1:
#         print(f"Elegiste la opcion {opcion}.")
#     case 2:
#         print(f"Elegiste la opcion {opcion}.")
#     case 3:
#         print(f"Elegiste la opcion {opcion}.")
#     case 4:
#         print(f"Elegiste la opcion {opcion}.")
#     case 5:
#         print(f"Elegiste la opcion {opcion}.")
#     case _:
#         print("Sos un pedazo de hijo de puta ☺") 

#
# Los inputs siempre devolveran valores de tipo string, por lo que si quiere evaluarse 
# en otro tipo de dato, se deberan mapear.



## para imprimir, existen dos maneras
# Directamente un dato o string.
# string = "texto"
# print(string)

# Imprimir con datos y strings concatenados.
# print(f"Mi cupleaños es {15}/{9}/{2000}")
#


## Estructuras de repeticion, o bucles. 
#  for i in range (x,y,z)      <-- Repetira y-x veces el bucle que se coloque debajo, saltando en intervalos z. 
#                                  En la variable i o contador, se ira acumulando en z el total de bucles realizados. 
#  El que modifica sus variables es puto. 
#  for element in collection:  <-- Recorrera toda la coleccion, guardando en element el objeto o dato actual. 
#
#  while(Condicion) <-- Evalua una condicion similar al if. En caso de ser verdadera, 
#            ejecuta el bucle y lo repetira hasta que sea falsa. Puede no hacerlo ninguna vez. 


# Programenme el FizzBuzz:
# Es un juego de petes. Van a imprimir una sucesion de numeros. Cuando el numero sea multiplo de 3, imprimime Fizz
# cuando sea multiplo de 5, imprimir Buzz. En caso de ser multiplo de 3 y de 5 (como el 15). FizzBuzz.



## Comparar multiples condiciones
## if (x == 1) and (y == 2):
    # print(cordenada 1,2)
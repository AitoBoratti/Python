# Python 

## Tipos de datos
### Datos primitivos:
* Int / Entero / Numero entero : 5
* Dato flotantes / reales / punto flotante: Numero con coma. 
* Char / Caracteres : a
* Bool / Booleanas / True False : Solo guardan el resultado de una operacion
        Booleana. True - False - None 
### Datos creados:
* String: Es una concatenacion de char, sirve para guardar palabras.
* Tuplas: Datos de valor constante, es decir, no modificables. Sirve para 
          guardar colecciones de datos cuyo valor se encuentra en conjunto.

## Operaciones de los tipos de datos.
Se prioriza la conservacion de los datos antes que la eficiencia. 
 
* Concatenacion: Es basicamente la suma, pero entre strings o chars/La adhicion de texto a un string. Todos los tipos de datos tendran valores literales.
* Mapeado, o conversion: En escencai, es forzar un tipo de dato a volverse otro.: tipo_de_dato_deseado(dato_a_convertir)

## Operaciones de numeros enteros y flotantes:
```py
    Numero1 = 5
    Numero2 = 3

    Numero1 += Numero2 "= 8"
    
    Numero1 -= Numero2 "= 2"
    
    Numero1 *= Numero2 "= 15"
    
    Numero1 /= Numero2 "= 5/3"

    Numero1 **= Numero2 "= 125"

    Numero1 = 10
    Numero2 = 3

    Modulo = Numero1 % Numero 2 "= 1"
```
## Operaciones booleanas:
* a == b:  Compara si A es equivalente B, devuelve true en caso de serlo, o false si no.
* a >= b:  Compara si A es mayor a B, devuelve true en caso de serlo, o false si no.
* a <= b:  Compara si A es menor a B, devuelve true en caso de serlo, o false si no.
* a != b:  Compara si A es diferente a B, devuelve true en caso de serlo, o false si no.

Todas las operaciones booleanas pueden ser anidadas de AND, OR, e incluso NOT para conseguir compararlas entre si. 

## Estructoras de control, la forma de contralar el flujo de un programa.

### El if es la forma mas basica de controlar el flujo de un programa, en caso de cumplir una condicion, accedera a ella. En caso de ser falso, se evaluara la siguiente, o se ira al else.
```py
    if (condicion):
    verdadera.

    elif (nueva condicion):
    segunda condicion verdadera.

    else
    falsa:
```
### El match (o case) sirve para evaluar condiciones de forma similar al if, pero es usado para evaluar el valor de un unico dato que puede tomar muchas opciones ( >4)
```py
    print("=== MENÚ PRINCIPAL ===")
    print("1. Ver perfil")
    print("2. Editar perfil")
    print("3. Configuración")
    print("4. Ayuda")
    print("5. Salir")
    print("======================")
    opcion = int(input("Por favor, elige una opción (1-5): "))

    match opcion:
        case 1:
            print(f"Elegiste la opcion {opcion}.")
        case 2:
            print(f"Elegiste la opcion {opcion}.")
        case 3:
            print(f"Elegiste la opcion {opcion}.")
        case 4:
            print(f"Elegiste la opcion {opcion}.")
        case 5:
            print(f"Elegiste la opcion {opcion}.")
        case _:
            print("Sos un pedazo de hijo de puta ☺") 
```

Los inputs siempre devolveran valores de tipo string, por lo que si quiere evaluarse 
en otro tipo de dato, se deberan mapear.



## para imprimir, existen dos maneras
Directamente un dato o string.
```py
    string = "texto"
    print(string)
```
Imprimir con datos y strings concatenados.
```py    
    print(f"Mi cupleaños es {15}/{9}/{2000}")
```


## Estructuras de repeticion, o bucles. 
El for:
 ```py
for i in range (x,y,z)      #<-- Repetira y-x veces el bucle que se 
        # continua el bucle         # coloque debajo, saltando en intervalos 
         
                                    # En la variable i o contador, se ira 
                                    # acumulando en z el total de bucles 
                                    # realizados. 
 ```                                
 ```py 
for element in collection:     #<-- Recorrera toda la coleccion, guardando 
                                #    en element el objeto o dato actual. 
```
El While: 
```py
 while(Condicion) <-- Evalua una condicion similar al if. En caso de ser verdadera, 
           ejecuta el bucle y lo repetira hasta que sea falsa. Puede no hacerlo ninguna vez. 
```

### Tipos de comentarios
* Summary: Se escriben dentro de triple comilla 
```py
    """
    Es un
    comentario
    multiple
    """
```
* Comentarios normales: Se marca su inicio con #. Solo cubre una linea. 
```py
    # Es un comentario de una linea
    ya no estoy comentado
```
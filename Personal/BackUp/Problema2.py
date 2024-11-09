""" Consigna
|Durante 5 días de la semana se quiere saber en una fábrica de cerámicos sobre la asistencia de sus empleados.
Cuántos faltaron por cada día por:

    • Enfermedad

    • Causas personales

    • licencia gremial

Al finalizar los 5 días de la semana que porcentaje tenemos de:

    • Enfermedad

    • Causas personales

    • licencia gremial
"""
from random import choice # Se utiliza esta funcion de la libreria random para ayudar a la automatizacion y el testo del programa. 

# Variables
empleados = [] # Lista Vacia donde guardar los empleados
Enfermedad = {"dia":0,"total":0}         # Variable de almacen de resultados, usamos un diccionario para facilitar el manejo de datos. (Asi no usamos dos variables por categoria.)
Causas_Personales = {"dia":0,"total":0}  # ↑ ↑ ↑ 
Licencia_Gremial = {"dia":0,"total":0}   # ↑ ↑ ↑ 
cantidad_empleados = int(input("Ingrese el total de empleados a procesar: ")) # Solicitamos el total de los empleados a procesar para crear nuestras listas.

# Procesos
def crearLista():
    
    # Si bien no se requiere el nombre del empleado, podriamos utilizar un diccionario para procesarlo y asi tener en cuenta su nombre
    empleados.extend({"nombre":choice(["Juan","Marcos","Jose","Aragon","Carlos"]),
                      "motivo_ausencia":choice(["Enfermedad","Causas_Personales","Licencia_Gremial","Asistio"])} for i in range(cantidad_empleados))
    
    # Si quisiera solamente guardarse el motivo de ausencia, podriamos usar el siguiente codigo : ↓
    """ Codigo Para solo Ausencias,
    empleados.extend(choice(["Enfermedad","Causas_Personales","Licencia_Gremial","Asistio"]) for i in range(cantidad_empleados))
    """           # Podria remplazerse choice por el codigo debajo y deberia funcionar igualmente. ↓
                  # input("Ingrese una de las siguientes condiciones de falta: Enfermedad, Causas Personales, Licencia Gremial")
                    
    # En caso de no tener un numero de empleados, podriamos emplear un while con alguna condicion de finalizacion tal como: ↓
    """ Alternativa con While,
    razon = ""
    while not (razon.lower() == Enfermedad or razon.lower() =="Causas_Personales" or razon.lower() == "Licencia_Gremial" ):
        razon=input("Ingrese el motivo de la ausencia: ")
        empleados.append({"nombre":input("Ingrese el nombre del empleado: ","motivo_ausencia":razon)})

    """
def reset():
    for empleado in empleados:
        empleado["motivo_ausencia"] = choice(["Enfermedad","Causas_Personales","Licencia_Gremial","Asistio"])
                     # Podria remplazerse choice por el codigo debajo y deberia funcionar igualmente.
                     # input("Ingrese una de las siguientes condiciones de falta: Enfermedad, Causas Personales, Licencia Gremial"
    """ Codigo Para Solo Ausencias,
    for i in range(len(empleados)):
        empleados[i] = choice(["Enfermedad","Causas_Personales","Licencia_Gremial","Asistio"])
    """

    Enfermedad["dia"]=0
    Causas_Personales["dia"]=0
    Licencia_Gremial["dia"]=0
def procesarFalta(empleado):
     match empleado:
            case "Enfermedad":
                Enfermedad["dia"] +=1
                Enfermedad["total"] +=1
            case "Causas_Personales":
                Causas_Personales["dia"] +=1
                Causas_Personales["total"] +=1
            case "Licencia_Gremial":
                Licencia_Gremial["dia"] +=1
                Licencia_Gremial["total"] +=1
def calcularFaltasDia():
    print(f"En el {i+1}° dia faltaron por...")
    print(f"Enfermedad: {Enfermedad['dia']}.")
    print(f"Causas Personales: {Causas_Personales['dia']}")
    print(f"Licencia Gremial:{Licencia_Gremial['dia']}\n")
def calcularPorcentaje():
    total = Causas_Personales["total"] + Enfermedad["total"] + Licencia_Gremial["total"]
    print(f"El porcentaje de personas que faltaron por Enfermedad fue de...           {round((Enfermedad['total']*100)/total,2)
                                                                                       if Enfermedad['total'] > 0 else 0}%")
    print(f"El porcentaje de personas que faltaron por Causas Personales fue de...    {round((Causas_Personales['total']*100)/total,2)
                                                                                       if Causas_Personales['total'] > 0 else 0}%")
    print(f"El porcentaje de personas que faltaron por Licencia Gremial fue de...     {round((Licencia_Gremial['total']*100)/total, 2)
                                                                                       if Licencia_Gremial['total'] > 0 else 0}%")

# Main
crearLista()
# Bucle principal. Aqui se realiza el proceso de empleados.
for i in range(5): 
    for empleado in empleados:
       procesarFalta(empleado["motivo_ausencia"])
    calcularFaltasDia()
    reset() # Reiniciamos los contadores diarios y cambiamos los motivos de falta para el proximo dia. 
calcularPorcentaje()
""" Consigna
En una competencia de 5 etapas tenemos 35 competidores de los cuales se distribuyen de la siguiente categorías:
    • 5 competidores de elite
    • 10 competidores Senior
    • 5 competidores Pre-Seniors
    • 15 competidores amateurs
Se quiere saber de cada una de las etapas
    • Cuántos abandonaron de cada categoría
Se quiere saber al finalizar la la competencia
    • Cuantos finalizaron la competencia por categoría
"""
from random import choice # Esto solo lo uso para hacer pruebas sin necesidad de ingresar datos de forma manual.

#Variables
competidores = []                                       # Lista Vacia donde almacenar a los competidores. 
resultados_elite = {"abandono":0, "completo":0}         # Variable de almacen de resultados, usamos un diccionario para facilitar el manejo de datos. (Asi no usamos dos variables por categoria.)
resultados_senior = {"abandono":0, "completo":0}        # ↑ ↑ ↑ 
resultados_pre_senior = {"abandono":0, "completo":0}    # ↑ ↑ ↑ 
resultados_amateurs = {"abandono":0, "completo":0}      # ↑ ↑ ↑ 

# Procedimientos
def cargarLista():
    competidores.extend("Elite" for i in range(5))
    competidores.extend("Senior" for i in range(10))
    competidores.extend("Pre-Seniors" for i in range(5))
    competidores.extend("Amateurs" for i in range(15))
def reset():
    resultados_elite["abandono"]=0
    resultados_senior["abandono"]=0
    resultados_pre_senior["abandono"]=0
    resultados_amateurs["abandono"]=0
def abandono(competidor):
    match competidor:
            case "Elite": resultados_elite["abandono"] += 1
            case "Senior": resultados_senior["abandono"] += 1
            case "Pre-Seniors": resultados_pre_senior["abandono"] += 1
            case "Amateurs": resultados_amateurs["abandono"] += 1
    competidores.remove(competidor)
def completo(competidor):
    match competidor:
            case "Elite": resultados_elite["completo"] += 1
            case "Senior": resultados_senior["completo"] += 1
            case "Pre-Seniors": resultados_pre_senior["completo"] += 1
            case "Amateurs": resultados_amateurs["completo"] += 1               
def resultados_etapa():

    print("Abandona la competicion, por categoria...")
    print(f"En la categoria de los Elite, abandonan: {resultados_elite['abandono']}. Abandonaron en total {resultados_elite['abandono']}.")
    print(f"En la categoria de los Senior, abandonan: {resultados_senior['abandono']}. Abandonaron en total {resultados_senior['abandono']}.")
    print(f"En la categoria de los Pre-senior, abandonan: {resultados_pre_senior['abandono']}. Abandonaron en total {resultados_pre_senior['abandono']}.")
    print(f"En la categoria de los Amateurs, abandonan: {resultados_amateurs['abandono']}. Abandonaron en total {resultados_amateurs['abandono']}.\n")
def resultados_finales():
    print("\nPara finalizar, completaron la competencia...")
    print(f"En la categoria de los Elite, completaron la competencia: {resultados_elite['completo']}")
    print(f"En la categoria de los Senior, completaron la competencia: {resultados_senior['completo']}")
    print(f"En la categoria de los Pre-senior, completaron la competencia: {resultados_pre_senior['completo']}")
    print(f"En la categoria de los Amateurs, completaron la competencia: {resultados_amateurs['completo']}")
            
# Main
cargarLista()
# Bucle principal. Aqui se simula la carrera.
for i in range(0,5):
    print(f"Inicia la {i+1}° etapa: ")
    for competidor in competidores[:]:                  # El [:] al final crea una copia de la lista sobre la cual iterar, ya que la modificaremos durante el bucle y asi nos evitamos problemas. 
        # res = input("Continua o Abandona? Y/N: ")     # Este seria una forma de que cada competidor diga si continua.
        # if (res.capitalize() == "N"):                 # ↑ ↑ ↑
        res = choice([True,True,False])                 # Para probar el ejercicio, lo haremos elegir de forma aleatoria, dandole el doble de chance de seguir. 
                                                        # Para entregar, seria mejor remplazar por lo forma manual. 
        if not res:
            abandono(competidor)
        elif (i==4):
                completo(competidor)
    resultados_etapa()
    reset() # Devolvemos los contadores de abandono a 0 para contarlos en la proxima etapa.
# Fin del Bucle. Solo falta la impresion de los resultados finales. 
resultados_finales()

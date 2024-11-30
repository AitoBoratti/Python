import pandas 

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# --------------------------------------- Solucion 1 ----------------------------------------------------
colors_data = {
    "fur_color": set(),
    "count":[0,0,0]
}

colors = data["Primary Fur Color"].tolist()

for color in colors:        
    if pandas.notna(color):
        colors_data["fur_color"].add(color)
    match color:
        case "Gray":
            colors_data["count"][0] += 1
        case "Cinnamon":
            colors_data["count"][1] += 1
        case "Black":
            colors_data["count"][2] += 1
                        
colors_data["fur_color"] = list(colors_data["fur_color"])

# new_data = pandas.DataFrame(colors_data)
# new_data.to_csv("Squirrel_Colors_Count.csv")

# Esta solucion, pese a ser mas larga y menos legible, tiene la ventaja de ser menos dependiente
# de la libreria pandas. Si bien aun la usa, seria sencillamente remplazable. El uso de sets puede
# ser confuso, sin embargo agiliza mucho el bucle principal.


# --------------------------------------- Solucion 2 ----------------------------------------------------
colors = data["Primary Fur Color"].value_counts(dropna=True).to_dict()
colors_data = {
    "fur_color" : list(colors.keys()),    # Equivalente a [key for key in colors.keys()],
    "count" :     list(colors.values())   # Equivalente a [value for value in colors.values()] 
}

# new_data = pandas.DataFrame(colors_data)
# new_data.to_csv("Squirrel_Colors_Count.csv")

# Esta solucion implementa la mayor cantidad de codigo panda, aprovechando muchisimos de sus metodos
# y siendo mas compacto, mientras que a su vez es facilmente legible. En general, es la mejor opcion
# pese a ser dependiente de la liberia pandas. 


# --------------------------------------- Solucion 3 ----------------------------------------------------
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])  # ← Esto devuelve todos las lineas en el archivo csv
                                                                      #   que contengan en la columna "Primary Fur Color" 
                                                                      #   el valor "Gray". Finalmente con "len" contamos. 
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

colors_data = {
    "fur_color":["Gray","Cinnamon","Black"],
    "count":[gray_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}
pandas.DataFrame(colors_data).to_csv("Squirrel_Colors_Count.csv")

# Esta solucion usa conceptos simples aprovechando que al hacer la busqueda de una serie en Pandas
# la libreria devuelve todas las lineas que coincidan con el valor, contandolas con el metodo len.
# Es muy eficiente y legible, pero los valores deben ser conocidos de antemano, por lo que no es 
# automatizable del todo.
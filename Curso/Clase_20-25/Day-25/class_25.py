import csv

with open("weather_data.csv",mode='r') as data_file:
    data = list(csv.reader(data_file))
    temperatures = [(int(row[1])) for row in data[1:]]

# print(temperatures)


# ----------------------------------------------------------------------------------------------------------------

import pandas   # Pandas Documentation: https://pandas.pydata.org/docs/


data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()

# avarege_temp = sum(data_list) / len(data_list)  # Obtener promedio sin pandas.
# print(round(avarege_temp))

# print(data["temp"].mean())                        # Obtener promedio con pandas.
# print(data["temp"].max())



# Obtener datos en columnas.
# print(data["temp"])                               # ← Ambos son equivalentes
# print(data.temp)                                  # ↑  

# Obetenr datos en filas
# print(data[data["day"] == "Monday"])              # Asi se obtiene la informacion de una fila. Se pasa como indice todo el DataFrame y se compara con lo buscado

max_temp = (data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
print(monday.condition)

temp_in_faren = (monday["temp"][0]  * 9/5) +32
print(temp_in_faren)


# Crear un nuevo DataFrame y guardarlo como csv
data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores"   : [76,56,65]
}

new_data = pandas.DataFrame(data_dict)     
new_data.to_csv("New_Data_Students.csv")
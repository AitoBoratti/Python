import pandas as pd

"""serie = pd.Series([ ])
print(serie)"""


data = {
    "Nombre":["Paco","Reborn","Hugo Boys","Bad Boys","Pibe",],
    "Precio":[5.0, 3.0, 2.0, 10.0, 1.0, ],
    "Cantidad Disponible": [10,20,30,5,15,]
}
# print(f"{dataFrame.iloc[0]}\n\n{dataFrame.iloc[1]}\n\n{dataFrame.iloc[2]}\n")
# print(f"{dataFrame.loc['D']}\n\n{dataFrame.loc['E']}")


dataFrame = pd.DataFrame(data)
dataFrame.loc[len(dataFrame)] = [None,None,None]
dataFrame = dataFrame._append({"Nombre":None,"Precio":None,"Cantidad Disponible":None}, ignore_index = True)

dataFrame = dataFrame.fillna(0)
print(dataFrame)

registro = {
    "nombre":"Aito",
    "edad":24
}

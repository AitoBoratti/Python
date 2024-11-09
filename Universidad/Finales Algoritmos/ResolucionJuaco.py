""" Consigna
    En una competencia de 5 etapas tenemos 35 competidores de los cuales se distribuyen de la siguiente categorías:
        • 5 competidores de elite
        • 10 competidores Senior
        • 5 competidores Pre_Seniors
        • 15 competidores amateurs
    Se quiere saber de cada una de las etapas
        • Cuántos abandonaron de cada categoría
    Se quiere saber al finalizar la competencia
        • Cuantos finalizaron la competencia por categoría
"""

competencia= []


for i in range(5):
    competencia.append("Elite")
    competencia.append("Pre_Seniors")
for i in range(10):
    competencia.append("Senior")
for i in range(15):
    competencia.append("Amateurs")




for i in range(5):
    Elite=0
    Pre_Seniors=0
    Senior=0
    Amateurs=0
    
    
    competencia_modificada = competencia
    
    for competidor in competencia:    
        res = input("Abandona la competencia? Y/N: ")
        if (res.capitalize() == "Y" ):
            match competidor:
                case "Elite": Elite += 1
                case "Senior": Senior += 1
                case "Pre_Seniors": Pre_Senior += 1
                case "Amateurs": Amateurs += 1
            competencia_modificada.remove(competidor)
        
            
            
    competencia = competencia_modificada
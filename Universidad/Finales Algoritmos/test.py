
from random import randint

inasistencia = 0
def faltas():
    cant = randint(0,10)
    for i in range(cant):
        inasistencia += 1

print(inasistencia)
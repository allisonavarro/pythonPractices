import random
import time
import numpy as np


def juego_tomb():
    numeros=[]
    generator= random.sample(range(1,76),75)
    numeros.append(generator)
    #print(numeros)



carton=[[2, 8, 3, 14, 4], [18, 16, 26, 19, 29], [35, 39, 'X', 40, 36], [58, 55, 51, 48, 59], [75, 61, 69, 71, 70]]



def check_and_replace(carton, bolita):
    for i in range(len(carton)):
        for j in range(len(carton[i])):
            if carton[i][j] == bolita:
                carton[i][j] = 0
    return carton


def check_zeros(lst):
    return [i for i, sublist in enumerate(lst) if all(elem == 0 for elem in sublist)]

for bolita in numeros[0]:
    #print(bolita)
    print(f"Bolita: {bolita}")
    carton = check_and_replace(carton, bolita)
    print(f"Updated Carton: {carton}")
    zero_brackets = check_zeros(carton)
    if zero_brackets:
     print("Ganaste felicidades")
     break

  
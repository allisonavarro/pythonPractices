import random
import time
import numpy as np

numeros=[]
generator= random.sample(range(1,76),75)
numeros.append(generator)
print(numeros)

replacement_value = 0

carton=[[2, 8, 3, 14, 4], [18, 16, 26, 19, 29], [35, 39, 'X', 40, 36], [58, 55, 51, 48, 59], [75, 61, 69, 71, 70]]



for bolita in numeros[0]:
    print(bolita)

    indice = np.where(carton == bolita)
    
    if indice[0].size > 0:
        carton[indice] = replacement_value
        print(str(indice) + " encontrado")
        break 
    else:(print("no esta"))
    #time.sleep(1)
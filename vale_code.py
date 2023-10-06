from random import sample
import numpy as np

import random

 

 

B=sample(range(1,15), 5)

I=sample(range(16,30), 5)

N=sample(range(31,45), 5)

G=sample(range(46,60), 5)

O=sample(range(61,75), 5)

 

resultado = [B, I , N, G, O]

 

 

for i in [B, I , N, G, O]:

    print(i)

transponidaMatrix = np.transpose(resultado)

print(transponidaMatrix)
import random
#Use the function for qty of boards for my players
def cartones(cantidad):
 
 serie = 1
 for _ in range(cantidad):
    arrays = []
    print("B  I  N  G  O")
    print("  N Serie " + str(serie))
    arrayB = random.sample(range(1,16), 5)
    arrays.append(arrayB)
    arrayI = random.sample(range(16,31), 5)
    arrays.append(arrayI)
    arrayN = random.sample(range(31,46), 4)
    arrayN.insert(2,'X')
    arrays.append(arrayN)
    arrayG = random.sample(range(46,61), 5)
    arrays.append(arrayG)
    arrayO = random.sample(range(61,76), 5)
    arrays.append(arrayO)
    imprimirCarton(arrays)
    serie = serie + 1

 return arrays


def imprimirCarton(the_carton):
 for row in zip(*the_carton):
        print("{:>2} {:>2} {:>2} {:>2} {:>2}".format(*row))




from cartones import cartones
#import tombola
#import revisor

myCarton=cartones(1)


def imprimirCarton():
 for row in zip(*myCarton):
        print("{:>2} {:>2} {:>2} {:>2} {:>2}".format(*row))


imprimirCarton()




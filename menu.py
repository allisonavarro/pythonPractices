import sys
from os import system
from cartones import cartones,imprimirCarton 


def display_menu(menu):
    
    for k, function in menu.items():
        print(k, function.__name__)

def Generador_de_cartones():
    qty_cartones=int(input("Seleccione la cantidad de cartones: "))

    jugadores=cartones(qty_cartones)
    #print(jugadores["serie1"])
    


    input("Presione Enter para comenzar\n")
   
    Comenzar(jugadores)
    input("Presione para sacar bolitar\n")

    

def Comenzar(jugadores):
    num_jugador=int(input("Escriba su numero de usuario: "))
    print("B  I  N  G  O")
    print("  N Serie " + str(num_jugador))
    imprimirCarton(jugadores["serie"+str(num_jugador)])
    
    input("Presione Enter para continuar\n")
    system('cls')  


def Salir():
    system('cls')  
    print("Adios")
    sys.exit()



def main():
   
    functions_names = [Generador_de_cartones, Salir]
    #description_names=['1. Generador de cartones','2.Comenzar juego','3.Salir']
    menu_items = dict(enumerate(functions_names, start=1))
    #print(menu_items)

    while True:
        display_menu(menu_items)
        selection = int(input("Seleccione la opcion: "))  
        selected_value = menu_items[selection]  
        selected_value() 

if __name__ == "__main__":
    main()
import sys
from os import system

def display_menu(menu):
    
    for k, function in menu.items():
        print(k, function.__name__)

def generador_de_cartones():
    print("uno")
    input("Presione Enter para continuar\n")
    system('cls')  # clears stdout

def dos():
    print("dos")
    # Simulate function output.
    input("Presione Enter para continuar\n")
    system('cls')  # clears stdout


def salir():
    system('cls')  # clears stdout
    print("Adios")
    sys.exit()

def main():
   
    functions_names = [generador_de_cartones, dos, salir]
    description_names=['1. Generador de cartones','2.Dos','3.Salir']
    menu_items = dict(enumerate(functions_names, start=1))
    print(menu_items)

    while True:
        display_menu(menu_items)
        selection = int(input("Seleccione la opcion: "))  
        selected_value = menu_items[selection]  
        selected_value() 

if __name__ == "__main__":
    main()
import sys
from os import system

def display_menu(menu):
    
    for k, function in menu.items():
        print(k, function.__name__)

def generadorCartones():
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
   
    functions_names = [generadorCartones, dos, salir]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(input("Seleccione la opcion: "))  
        selected_value = menu_items[selection]  
        selected_value() 

if __name__ == "__main__":
    main()
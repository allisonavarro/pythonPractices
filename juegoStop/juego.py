import time

def inicio():
    letter = input("Ingrese la letra para jugar ")
    words = create_dict(letter)
    return(words)



def create_dict(dict_name):
         dict_name = {
        'Nombre': [],
        'Comida': [],
        'Pais': [],
        'Objeto': [],
        'Animal': [],
        'Apellido': [],
        } 
         return dict_name



def play():
    categories=inicio()
    points=create_dict("points")
    start_time=time.time()
    for key in categories:
             word = input("Ingrese una palabra de la categoria " + str(key) + " ")
             categories[key]=word
    end_time=time.time()
    print("Stooop, su tiempo fue de " +str(end_time-start_time) + " segundos")
    print("Revisemos el stop para asignar puntos")
    

    for key, value in categories.items():
          print(f"{key}: {value}")
          puntaje=input("El puntaje a asignar es de " )
          points[key]=int(puntaje)
    total= sum(points.values())      
    print("El puntaje total es de " + str(total))      

play()
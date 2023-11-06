from tkinter import *
from time import strftime

reloj = Tk()
reloj.title('Esta es la hora')


def time():
	laHora = strftime('%H:%M:%S %p')
	clock.config(text = laHora)
	clock.after(1000, time)


clock = Label(reloj, font = ('arial', 40, 'bold'), background = 'yellow', foreground = 'black')
clock.pack(anchor = 'center')
time()

mainloop()
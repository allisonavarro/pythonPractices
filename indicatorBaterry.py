from tkinter import *
from time import strftime
import psutil

reloj = Tk()
reloj.title('estado de bateria')


def time():
	battery = psutil.sensors_battery()
	percent = battery.percent
	plugged = battery.power_plugged
	status = "Conectada" if plugged else "No conectada"
	laBateria = f"Bateria: {percent}%, {status}"
	clock.config(text = laBateria)
	clock.after(1000, time)


clock = Label(reloj, font = ('arial', 25, 'bold'), background = 'yellow', foreground = 'black')
clock.pack(anchor = 'center')
time()

mainloop()
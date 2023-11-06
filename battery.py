import psutil

from tkinter import *
indicator = Tk()

def update_indicator():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged
    status = "Conectada" if plugged else "No conectada"
    text.set(f"Bateria: {percent}%, {status}")
    root.after(5000, update_indicator)  # Update every 5 seconds

root = Tk()
text = StringVar()
label =  Label(root, textvariable=text)
label.pack()
update_indicator()          
root.mainloop()
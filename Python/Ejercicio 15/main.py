import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0,weight=1)

label_saludo = ttk.Label(window, text="Buenas! Este es el ejercicio 15")
label_saludo.grid(column=0,row=0,padx=5,pady=5)

numeros = [1,2,3,4,5,6]

for pos in range(0,len(numeros)):
    curr_numero = ttk.Checkbutton(window,text=numeros[pos] , takefocus=0)
    curr_numero.grid(column=0,row=pos+1)

window.mainloop()
import tkinter
from tkinter import ttk


botones = ["A","B","C","D","E"]

def selected_opcion():
    label_seleccion.config(text=f'Elemento {str(seleccion.get())} seleccionado!')

def click_reinicio():
    hijos = window.winfo_children()
    for hijo in hijos:
        if isinstance(hijo,ttk.Radiobutton):
            hijo.state(["!focus","!selected"])
        elif isinstance(hijo,ttk.Label):
            hijo.config(text="Elemento no seleccionado")

window = tkinter.Tk()

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

label_seleccion = ttk.Label(window, text="Elemento no seleccionado")
label_seleccion.grid(column=0, row=6, padx=10, pady=10)

seleccion = tkinter.IntVar()

for pos in range(0, len(botones)):
    curr_btn = ttk.Radiobutton(window, text=botones[pos], value=pos+1 ,  variable=seleccion, command=selected_opcion)
    curr_btn.grid(column=0, row=pos, padx=10, pady=10)

btn_reinicio = ttk.Button(window, text="Reiniciar!" , command=click_reinicio)
btn_reinicio.grid(column=0,row=7)

window.mainloop()
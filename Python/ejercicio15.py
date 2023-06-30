import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

ventana.columnconfigure(0, weight= 1)
ventana.columnconfigure(1, weight= 3)

lista = ["Pyton", "SQL", "Java", "HTML"]
lista_items = tkinter.StringVar(value=lista) 
list_box = tkinter.Listbox(ventana, height= 5, listvariable= lista_items)
list_box.grid(column= 0, row= 0, sticky= tkinter.W, padx= 5, pady= 5)

label = ttk.Label(ventana, text = "Mi nombre es Pedro")
label.grid(column= 0, row= 1, sticky= tkinter.W, padx= 5, pady= 5)

ventana.mainloop()

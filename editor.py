import tkinter as tk
from tkinter import filedialog # Para el manejo de archivos

# Funciones

def nuevo():
    lower_text.set("Nuevo fichero")

def abrir(): 
    lower_text.set("Abrir fichero")

def guardar(): 
    lower_text.set("Guardar fichero")

def open_readme(): 
    lower_text.set("Abrir fichero README.md")

# Interfaz de usuario
## Ventana principal

root = tk.Tk()
root.title("Editor de texto")

## Barra de menú

menubar = tk.Menu(root)
root.config(menu=menubar)
archive = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=archive)
archive.add_command(label="Nuevo", command=nuevo)
archive.add_command(label="Abrir", command=abrir)
archive.add_command(label="Guardar", command= guardar)
archive.add_command(label="Cerrar")

help = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=help)
help.add_command(label = "Acerca de...", command= open_readme)

## Ventana de texto

texto = tk.Text(root)
texto.pack(fill="both", expand=1)
texto.config(padx=6, pady=4, bd=0, font=("Consolas", 12))

## Mensaje inferior
lower_text = tk.StringVar()
lower_text.set("Bienvenido al editor de texto")
lower_info = tk.Label(root, textvariable=lower_text, justify="right")
lower_info.pack(side="left")


# Enlazar funciones con los botones del menu



# Bucle Principal
root.mainloop()

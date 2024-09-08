import tkinter as tk
from tkinter import filedialog # Para el manejo de archivos

# Interfaz de usuario

ventana_editor = tk.Tk()
ventana_editor.title("Editor de texto")
ventana_editor.config(background="Black", width=600, height=600)

entrada_editor = tk.Text(ventana_editor, wrap="word", undo=True)
entrada_editor.pack(expand=1, fill="both"   )





# Bucle Principal
ventana_editor.mainloop()

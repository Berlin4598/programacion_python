import tkinter as tk  #exportamos libreria tkinter y le ponemos un alias (tk)
from tkinter import ttk #importamos ttk para usar estilos y temas en tkinter

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800  # Definir el ancho de la ventana
alto_ventana = 600  # Definir el alto de la ventana
size = f"{ancho_ventana}x{alto_ventana}"  # Definir el tamaño de la ventana
ventana.geometry(size)

ventana.title("Mi primera ventana")  # Titulo de la ventana

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")
#"copy path" de la imagen

ventana.mainloop()  # Iniciar el bucle principal de la ventana, siempre va al final
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
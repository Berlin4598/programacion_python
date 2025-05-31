import tkinter as tk  #exportamos libreria tkinter y le ponemos un alias (tk)
from tkinter import ttk #importamos ttk para usar estilos y temas en tkinter

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800  # Definir el ancho de la ventana
alto_ventana = 600  # Definir el alto de la ventana
size = f"{ancho_ventana}x{alto_ventana}"  # Definir el tamaño de la ventana
ventana.geometry(size)

ventana.title("botones")

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")
#"copy path" de la imagen

def show_name():
    print(entrada.get()) #el get va a devolver texto que ingresemos en la entrada


btn = tk.Button(ventana, text="Boton 1", relief="flat", bg="lightpink", command=show_name)
#x para los lados
#y para abajo y arriba

btn.pack(pady=30, ipady=30)

labels = tk.Label(ventana, text="ingresa tu nombre").pack(pady=10)


entrada = tk.Entry(ventana, width=100)
entrada.pack(pady=10)


ventana.mainloop()  # Iniciar el bucle principal de la ventana, siempre va al final
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
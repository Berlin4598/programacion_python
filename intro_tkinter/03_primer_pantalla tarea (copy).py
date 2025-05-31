import tkinter as tk  #exportamos libreria tkinter y le ponemos un alias (tk)
from tkinter import ttk
from turtle import color #importamos ttk para usar estilos y temas en tkinter

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800  # Definir el ancho de la ventana
alto_ventana = 600  # Definir el alto de la ventana
size = f"{ancho_ventana}x{alto_ventana}"  # Definir el tamaño de la ventana
ventana.geometry(size)

ventana.title("Mi primer ventana")

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")
#"copy path" de la imagen

#metodo row/columnconfigure (row=fila, column=columna)
#la variable ventana, fila configurar, numero de fila, peso
ventana.rowconfigure(0, weight=1) #fila 0
ventana.rowconfigure(1, weight=1) #fila 1
ventana.rowconfigure(2, weight=1) #fila 2
ventana.rowconfigure(3, weight=1) #fila 3
ventana.rowconfigure(4, weight=1) #fila 4

#columnas
ventana.columnconfigure(0, weight=1) #columna 0
ventana.columnconfigure(1, weight=1) #columna 1
ventana.columnconfigure(2, weight=1) #columna 2
ventana.columnconfigure(3, weight=1) #columna 3
ventana.columnconfigure(4, weight=1) #columna 4


btn1 = tk.Button(ventana, text="Mercado soriana", bg="#FFA500", fg="black", relief="raised", font=("Arial", 10))
btn1.grid(row=0, column=0, columnspan=2, sticky="new")

btn0 = tk.Button(ventana, text="Boton 0", bg="#FFB6C1", fg="black", relief="raised", font=("Arial", 10))
btn0.grid(row=0, column=0, sticky="s")

btn = tk.Button(ventana, text="Boton 1", bg="#FFB6C1", fg="black", relief="raised", font=("Arial", 10))
btn.grid(row=1, column=1, sticky="n")  #queremos el boton en la fila 1

btn = tk.Button(ventana, text="Boton 2", bg="#FFB6C1", fg="black", relief="raised", font=("Arial", 10))
btn.grid(row=2, column=2, sticky="n")

btn = tk.Button(ventana, text="Boton 3", bg="#FFB6C1", fg="black", relief="raised", font=("Arial", 10))
btn.grid(row=3, column=3, sticky="n")

#boton 4
btn = tk.Button(ventana, text="Boton 4", bg="#FFB6C1", fg="black", relief="raised", font=("Arial", 10))
btn.grid(row=4, column=4, sticky="n") #el metodo sticky lo pone al norte

ventana.mainloop()  # Iniciar el bucle principal de la ventana, siempre va al final
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
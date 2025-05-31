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

#metodo row/columnconfigure (row=fila, column=columna)
#la variable ventana, fila configurar, numero de fila, peso
ventana.rowconfigure(0, weight=2) #fila 0
ventana.rowconfigure(1, weight=1) #fila 1
ventana.rowconfigure(2, weight=1) #fila 2

#columnas
ventana.columnconfigure(0, weight=2) #columna 0
ventana.columnconfigure(1, weight=1) #columna 1
ventana.columnconfigure(2, weight=1) #columna 2

btn = ttk.Button(ventana, text="boton 1")
btn.grid(row=0, column=0, sticky="n")  #queremos el boton en la fila 1

btn = ttk.Button(ventana, text="boton 2")
btn.grid(row=1, column=1, rowspan=2, sticky="ns") #rowspan ocupa dos filas 
#el sticky ns toma todo el ancho de la celda

btn = ttk.Button(ventana, text="boton 3")
btn.grid(row=2, column=2)

#boton 4
btn = ttk.Button(ventana, text="boton 4")
btn.grid(row=0, column=0, sticky="s") #el metodo sticky lo pone al norte

#boton 5
btn = ttk.Button(ventana, text="boton 5")
btn.grid(row=0, column=0, sticky="e")

#boton 6
btn = ttk.Button(ventana, text="boton 6")
btn.grid(row=0, column=0, sticky="w")

#boton 7
btn = ttk.Button(ventana, text="boton 7")
btn.grid(row=0, column=0) #no poner el stiky para dejar el boton en medio
#(nsew) absorbe todo el espacio disponible, agranda el boton

ventana.mainloop()  # Iniciar el bucle principal de la ventana, siempre va al final
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
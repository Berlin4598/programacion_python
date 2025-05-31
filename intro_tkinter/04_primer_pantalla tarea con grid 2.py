import tkinter as tk  #importamos libreria tkinter y le ponemos un alias (tk)
from tkinter import ttk
import random #importamos la librería random para generar colores aleatorios
from turtle import color #importamos ttk para usar estilos y temas en tkinter

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800  # Definir el ancho de la ventana
alto_ventana = 600  # Definir el alto de la ventana
size = f"{ancho_ventana}x{alto_ventana}"  # Definir el tamaño de la ventana
ventana.geometry(size)

ventana.title("Mi primer ventana") #titulo de mi ventana

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")
#"copy path" de la imagen

#lista de colores de los cuales se va a elegir uno random
colores = [
    "fuchsia", "blue", "brown", "grey", "coral",
    "salmon", "cyan", "purple", "pink", "white",
    "red", "yellow", "green", "salmon", "orange"
]

#crear los botones, acomodarlos y darles su estilo
for row in range(12): #usamos este for para recorrer las filas, empezamos entrando en la 0
    ventana.rowconfigure(row, weight=1) #usamos este for para las filas, por lo que iré creando las 12
    for column in range(12):
        ventana.columnconfigure(column, weight=1) #creo las columnas
        btn = tk.Button(ventana, text=f"Botón {column + 1}", bg=random.choice(colores))
        btn.grid(row=row, column=column, sticky="nsew")

#ejecutamos la ventana infinitamente
ventana.mainloop()
import tkinter as tk  #exportamos libreria tkinter y le ponemos un alias (tk)
from tkinter import ttk #importamos ttk para usar estilos y temas en tkinter

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800  # Definir el ancho de la ventana
alto_ventana = 600  # Definir el alto de la ventana
size = f"{ancho_ventana}x{alto_ventana}"  # Definir el tamaño de la ventana
ventana.geometry(size)

ventana.title("entry")

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")
#"copy path" de la imagen

ventana.columnconfigure(0, weight=2)  # Configurar la columna 0 para que ocupe todo el espacio disponible
ventana.columnconfigure(1, weight=2)
ventana.columnconfigure(2, weight=2) # Configurar la fila 0 para que ocupe todo el espacio disponible

label = tk.Label(ventana, text="ingresa el primer numero: ", font=("Arial", 30), fg="pink")  # Crear una etiqueta con un texto y una fuente
label.grid(column=1, sticky="n", row=0)
entrada = tk.Entry(ventana, font=("Arial", 20))  # Crear un campo de entrada de texto
entrada.grid(column=1, row=1, sticky="n", pady=10)

label2 = tk.Label(ventana, text="ingresa el segundo numero: ", font=("Arial", 30), fg="pink")  # Crear una etiqueta con un texto y una fuente
label2.grid(column=1, sticky="n", row=2)
entrada2 = tk.Entry(ventana, font=("Arial", 20))  # Crear un campo de entrada de texto
entrada2.grid(column=1, sticky="n", pady=10)

def sumar():
    suma.config(text=f"suma:  {int(entrada.get()) + int(entrada2.get())}")
suma = tk.Label(ventana, font=("Arial", 30), fg="purple")  # Crear una etiqueta para mostrar el resultado
suma.grid(column=1, row=4)
btn = tk.Button(ventana, text="Sumar", relief="flat", bg="pink", command=sumar)
btn.grid(column=1, pady=3.5)

def restar():
    resta.config(text=f"resta:  {int(entrada.get()) - int(entrada2.get())}")
resta = tk.Label(ventana, font=("Arial", 30), fg="violet")  # Crear una etiqueta para mostrar el resultado
resta.grid(column=1, row=4)
btn = tk.Button(ventana, text="Restar", relief="flat", bg="pink", command=restar)
btn.grid(column=1, pady=3.5)

def multiplicar():
    mult.config(text=f"multiplicacion:  {int(entrada.get()) * int(entrada2.get())}")
mult = tk.Label(ventana, font=("Arial", 30), fg="purple")  # Crear una etiqueta para mostrar el resultado
mult.grid(column=1, row=4)
btn = tk.Button(ventana, text="Multiplicar", relief="flat", bg="pink", command=multiplicar)
btn.grid(column=1, pady=3.5)

def dividir():
    div.config(text=f"division:  {int(entrada.get()) / int(entrada2.get())}")
div = tk.Label(ventana, font=("Arial", 30), fg="violet")  # Crear una etiqueta para mostrar el resultado
div.grid(column=1, row=4)
btn = tk.Button(ventana, text="Dividir", relief="flat", bg="pink", command=dividir)
btn.grid(column=1, pady=3.5)

ventana.mainloop()  # Iniciar el bucle principal de la ventana, siempre va al final
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
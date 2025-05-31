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
ventana.columnconfigure(1)
ventana.columnconfigure(2, weight=2) # Configurar la fila 0 para que ocupe todo el espacio disponible

label = tk.Label(ventana, text="ingresa tu nombre: ", font=("Arial", 30), fg="red")  # Crear una etiqueta con un texto y una fuente
label.grid(column=1, sticky="n", row=1)

entrada = tk.Entry(ventana, font=("Arial", 20))  # Crear un campo de entrada de texto
entrada.grid(column=1, sticky="n", pady=10)
#texto predefinido en la entrada
#entrada.insert(0, "escribe tu nombre")
#devuelve el texto que hay dentro de la entrada
#entrada.get()

def click():
    show_name.config(text=f"Hola, {entrada.get()}")

show_name = tk.Label(ventana, font=("Arial", 30), fg="blue")
show_name.grid(column=1, row=0)
btn = tk.Button(ventana, text="Enviar", relief="flat", bg="pink", command=click)
btn.grid(column=1)

ventana.mainloop()  # Iniciar el bucle principal de la ventana, siempre va al final
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
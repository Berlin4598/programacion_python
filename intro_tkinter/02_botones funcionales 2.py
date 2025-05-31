import tkinter as tk  #exportamos libreria tkinter y le ponemos un alias (tk)
from tkinter import ttk #importamos ttk para usar estilos y temas en tkinter
#tkinter es una libreria para crear interfaces graficas

ventana = tk.Tk()  # Crear una ventana principal
#instanciar la clase = crear un objeto (ventana) que viene de la clase tk

ancho_ventana = 800  # Definir el ancho de la ventana
alto_ventana = 600  # Definir el alto de la ventana
size = f"{ancho_ventana}x{alto_ventana}"  # Definir el tamaño de la ventana
ventana.geometry(size) # Definir el tamaño de la ventana (ancho x alto)

ventana.title("Mi primer ventana")  # Establecer el título de la ventana xon el método title
#es el texto que aparece arriba (titulo)

#para cambiar el icono de la ventana hay que guardar las imagenes con el formato .ico
ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")
#"copy path" de la imagen, cambiar todas las barras por / y poner el nombre de la imagen con su extension


#crear funcion para el boton
def click():
    print("Hola soy un boton") #imprimir en la consola el texto que queramos

boton = ttk.Button(ventana, text="hola soy un boton", command=click) # Crear un botón con ttk
boton.pack() # Añadir el botón visible a la ventana con el método pack


#colorcodes pagina para colores en codigo hexadecimal
def estilo():
    print("cambiando estilo de boton")
    boton2.config(bg="blue", fg="white", relief="sunken", text="cambiaste mi estilo") #background, color de letra, relieve
    print("cambiamos los estilos del boton2")
boton2 = tk.Button(ventana, text="tocame para cambiar mi estilo", command=estilo) # Crear un botón con tk
boton2.pack() # Añadir el botón visible a la ventana con el método pack

#final
ventana.mainloop()  # Iniciar el bucle principal de la ventana
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
import tkinter as tk
from tkinter import ttk, messagebox as mb

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800 
alto_ventana = 600  
size = f"{ancho_ventana}x{alto_ventana}" 
ventana.geometry(size)

ventana.title("ventanas emergentes")

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")

def show_windos():
    mb.showinfo("Explicacion de show info", "esta es una ventana emergente de informacion. El icono que tiene es el de una i (denotando la info)\n"
                                                   "y el texto que tiene es el que le pasamos como argumento, además se le puede poner un titulo. Presiona aceptar para cerrarla")  
    mb.showwarning("Explicacion de show warning", "esta es una ventana emergente de advertencia. El icono que tiene es el de una i dentro de un triangulo amarillo\n"
                                                   "y el texto que tiene es el que le pasamos como argumento, además se le puede poner un titulo, al giaul que a todas las ventanas emergentes. Preciona aceptar para ver la siguiente ventana.")
    mb.showerror("Explicacion de show error", "esta es una ventana emergente de errores. El icono que tiene es el de una x, en color rojo, que alerta más al usuario de un error\n"
                                                   "este texto, al giual que en las otras ventanas, es uno de los argumentos que le pasamos a la funcion, además del titulo. Preciona aceptar.")
    result = mb.askyesno("Pregunta", "quieres drogas?")
    msg = ttk.Label(ventana, font=("Arial",20), foreground="pink")
    if result:
        msg.config(text="si te venden drogas te van a decir, que se siente muy padre y te vas a reir")
        msg.pack()
    else:
        msg.pack()
        msg.config(text="que aburrido")


btn = ttk.Button(ventana, text="Mostrar ventanas emergentes", command=show_windos)
btn.pack()

ventana.mainloop()
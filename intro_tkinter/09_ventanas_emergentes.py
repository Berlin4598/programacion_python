import tkinter as tk  #exportamos libreria tkinter y le ponemos un alias (tk)
from tkinter import ttk, messagebox as mb

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800  # Definir el ancho de la ventana
alto_ventana = 600  # Definir el alto de la ventana
size = f"{ancho_ventana}x{alto_ventana}"  # Definir el tamaño de la ventana
ventana.geometry(size)

ventana.title("ventanas emergentes")

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")
#"copy path" de la imagen

#ventanas emgergentes (informan errores o advertencias)
def show_windos():
    mb.showinfo("Ventana emergente de informacion", "nopasana")
    mb.showwarning("Ventana de advertencia", "yameroyama")
    mb.showerror("ventana emergente de error", "yama")
    #eliminar registros
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

ventana.mainloop()  # Iniciar el bucle principal de la ventana, siempre va al final
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
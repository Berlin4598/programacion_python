import tkinter as tk  
from tkinter import ttk

ventana = tk.Tk()

ancho_ventana = 800
alto_ventana = 600  
size = f"{ancho_ventana}x{alto_ventana}"  
ventana.geometry(size)

ventana.title("ventana con 5 botones")

ventana.iconbitmap("C:/Users/danay/Desktop/simple-python-project/intro_tkinter/icono_calavera.ico")

def click1():
    boton1.config(bg="yellow", fg="black", relief="sunken", text="una desolacion")
    print("soy como un lamento")
boton1 = tk.Button(ventana, text="es mi situacion", command=click1) 
boton1.pack()

def click2():
    boton2.config(bg="black", fg="white", relief="groove", text="que un dia empezo")
    print("y no va a terminar")
boton2 = tk.Button(ventana, text="lamento boliviano", command=click2) 
boton2.pack() 

def click3():
    boton3.config(bg="red", fg="white", relief="flat", text="ohhhhhhhhhh")
    print("oh oh oh oh oh ohhhhhhh")
boton3 = tk.Button(ventana, text="ya nadie hace daño", command=click3) 
boton3.pack() 

def click4():
    boton4.config(bg="white", fg="black", relief="raised", text="yeeeehhhhhhhhhhh")
    print("y yo estoy aquí")
boton4 = tk.Button(ventana, text="yeh yeh yehhhhhhhhhhh", command=click4) 
boton4.pack()

def click5():
    boton5.config(bg="orange", fg="green", relief="ridge", text="y mi corazon idiota")
    print("siempre brillaraaaaaaaaaaa a a a a a")
boton5 = tk.Button(ventana, text="borracho y locoooooooooo", command=click5) 
boton5.pack()


#final
ventana.mainloop()  # Iniciar el bucle principal de la ventana
#esto hace que siempre se este abriendo la ventana y no se cierre al instante
import tkinter as tk 
from tkinter import ttk, messagebox as mb
from datetime import datetime

ventana = tk.Tk()  # Crear una ventana principal

ancho_ventana = 800  
alto_ventana = 600  
size = f"{ancho_ventana}x{alto_ventana}"  
ventana.geometry(size)

ventana.title("Formulario para usuarios")  

#crear filas y columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=2)
ventana.columnconfigure(2, weight=1)

cliente = {
    "name": "",
    "phone": "",
    "address":"",
    "created_at": datetime.now(),
}

def guardar_datos():
    cliente["name"] = entry_name.get()
    cliente["phone"] = entry_phone.get()
    cliente["address"] = entry_address.get()
    print(cliente)
    mb.showinfo("Información", "Cliente guardado con éxito")

label = tk.Label(ventana, text="Formulario para crear Clientes ", font=("Arial", 20), fg="black")
label.grid(column=1, sticky="n", row=0)

label = tk.Label(ventana, text="Nombre: ", font=("Arial", 15), fg="black")
label.grid(column=1, sticky="n", pady=10)
entry_name= tk.Entry(ventana, font=("Arial", 20))
entry_name.grid(column=1, sticky="n", pady=10)

label = tk.Label(ventana, text="Teléfono: ", font=("Arial", 15), fg="black")
label.grid(column=1, sticky="n", pady=10)
entry_phone = tk.Entry(ventana, font=("Arial", 15))
entry_phone.grid(column=1, sticky="n", pady=10) 

label = tk.Label(ventana, text="Dirección: ", font=("Arial", 15), fg="black")
label.grid(column=1, sticky="n", pady=10)
entry_address = tk.Entry(ventana, font=("Arial", 15)) 
entry_address.grid(column=1, sticky="n", pady=10) 

btn = tk.Button(ventana, text="Guardar", relief="flat", bg="yellow", command=guardar_datos)
btn.grid(column=1)


ventana.mainloop()
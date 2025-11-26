import tkinter as tk
from PIL import Image,ImageTk
def saludar():
    etiqueta.set("hola")
    
ventana=tk.Tk()
ventana.title("biblioteca")
ventana.geometry("300x400")
top=tk.Frame(ventana,bg="skyblue")
top.pack(fill="x")
content=tk.Frame(ventana,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
tk.Label(top,text="Biblioteca",bg="skyblue",font=("Arial",24)).pack()
botonL=tk.Button(content,text="Libros",command=saludar).grid(row=0,column=0,padx=10,pady=10)
botonA=tk.Button(content,text="Autores",command=saludar).grid(row=1,column=0,padx=10,pady=10)
botonH=tk.Button(content,text="Horario",command=saludar).grid(row=0,column=1,padx=10,pady=10)
botonP=tk.Button(content,text="Prestamos",command=saludar).grid(row=1,column=1,padx=10,pady=10)
imagen=Image.open("biblio.png")
imagen=ImageTk.PhotoImage(imagen)
label=tk.Label(content,image=imagen)
label.grid(row=2,column=0,columnspan=2)
ventana.mainloop()



"""texto=tk.Label(ventana,text="hola").pack(side="top")




boton=tk.Button(ventana,text="boton",command=saludar).pack(side="left")
etiqueta=tk.StringVar()
tk.Label(ventana,textvariable=etiqueta).pack(side="right")
ventana.mainloop()
"""

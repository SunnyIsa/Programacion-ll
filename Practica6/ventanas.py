import tkinter as tk
from tkinter import messagebox
import bibli as BI
import json
import os
def alertaS():
        messagebox.showinfo("Alerta","seleccion invalida:\n debe seleccionar un elemento de la lista")
def alertaL():
        messagebox.showinfo("Alerta","Estas intentando ingresar un libro vacio?")
def alertaT():
        messagebox.showinfo("Alerta","no escribiste nada")

#INICIO
def irRegistroB():
    inicio.withdraw()
    registroB.deiconify()
    actualizarB()
def irIngreso1():
    inicio.withdraw()
    ingreso.deiconify()




inicio=tk.Tk()
inicio.title("inicio")
inicio.geometry("600x500")

top=tk.Frame(inicio,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(inicio,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)


tk.Label(top,text="Biblioteca",bg="skyblue",font=("Arial",24)).pack()

btnRegistrar = tk.Button(content,text="Registrar",command=irRegistroB)
btnRegistrar.grid(row=0, column=0)

btnEliminar = tk.Button(content,text="Ingresar",command=irIngreso1)
btnEliminar.grid(row=1, column=0)



Logito = tk.PhotoImage(file="logoBI.png")
lbl_img = tk.Label(content, image = Logito)
lbl_img.grid(row=0, column=1, rowspan=2)




#registro de biblioteca



def irInicio1():
    registroB.withdraw()
    inicio.deiconify()
def registrarB():
    try:
        n=nombre.get()
        d=dias.get()
        a=ap.get()
        c=ci.get()
        i=int(id.get())
        s=BI.Biblioteca(n,d,a,c,i)
        BI.agregar(s)
        actualizarB()
        limpiarCamposB()
    except:
        alertaT()
    
def limpiarCamposB():
    nombre.set("")
    dias.set("")
    ap.set("")
    ci.set("")
    id.set("")
    
def actualizarB():
        listboxB.delete(0, tk.END)
        if not os.path.exists("general.bin")  or os.path.getsize("general.bin")==0:
                s=[]
        else:
                with open("general.bin","r") as f:
                        s=json.load(f)
                
        for b in s:
                l=b["nombre"]+" "+str(b["ID"])
                listboxB.insert(tk.END, l)
        limpiarCamposB()
def eliminarB():
    try:
        s=listboxB.curselection()[0]
        with open("general.bin","r") as f:
            l=json.load(f)
        d=BI.Biblioteca(l[s]["nombre"],"","","",l[s]["ID"])
        d.borrarL()
        d.borrarA()
        d.borrarPR()
        BI.borrar(d)
        actualizarB()
    except:
        alertaS()



registroB=tk.Toplevel(inicio)

registroB.title("registro de bibliotecas")
registroB.geometry("600x500")

top=tk.Frame(registroB,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(registroB,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
content.columnconfigure(2,weight=2)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)
content.rowconfigure(3,weight=1)
content.rowconfigure(4,weight=1)
content.rowconfigure(5,weight=1)

tk.Label(top,text="Biblioteca",bg="skyblue",font=("Arial",24)).pack()

#texto y entradas
nombre=tk.StringVar()
lblUsuario = tk.Label(content,text="Nombre:",bg="white")
txtUsuario = tk.Entry(content,textvariable=nombre)

lblUsuario.grid(row=0, column=0)
txtUsuario.grid(row=0, column=1)

dias=tk.StringVar()
lblApertura = tk.Label(content,text="Dias de apertura:",bg="white")
txtApertura = tk.Entry(content,textvariable=dias)

lblApertura.grid(row=1, column=0)
txtApertura.grid(row=1, column=1)

ap=tk.StringVar()
lblHdApertura = tk.Label(content,text="Hora de apertura:",bg="white")
txtHdApertura = tk.Entry(content,textvariable=ap)


lblHdApertura.grid(row=2, column=0)
txtHdApertura.grid(row=2, column=1)

ci=tk.StringVar()
lblHdCierre = tk.Label(content,text="Hora de cierre:",bg="white")
txtHdCierre = tk.Entry(content,textvariable=ci)

lblHdCierre.grid(row=3, column=0)
txtHdCierre.grid(row=3, column=1)

id=tk.StringVar()
lblID = tk.Label(content,text="ID:",bg="white")
txtID = tk.Entry(content,textvariable=id)

lblID.grid(row=4, column=0)
txtID.grid(row=4, column=1)

btnRegistrar = tk.Button(content,text="Registrar",command=registrarB)
btnRegistrar.grid(row=5, column=0)

btnEliminar = tk.Button(content,text="Eliminar",command=eliminarB)
btnEliminar.grid(row=5, column=1)

btnSalir = tk.Button(content,text="Salir",command=irInicio1)
btnSalir.grid(row=5, column=2)
B=0
listboxB= tk.Listbox(content,width=30, height=18, bg="white", font=("Arial",12))
listboxB.grid(row=0, column=2, rowspan=5)




#listbox.config(heigth=listbox.size())

registroB.withdraw()



#Ingreso


def irInicio2():
    ingreso.withdraw()
    inicio.deiconify()
def limpiarCamposI():
    nombreI.set("")
    idI.set("")

def irEbiblioteca1():
    try:
        global IDB
        n=nombreI.get()
        IDB=int(idI.get())
        s=BI.Biblioteca(n,"","","",IDB)
        B=BI.buscar(s)
        actualizarL()
        if B!=None:
            t="Horario: \n "+"Dias de apertura: "+B["horario"]["dias"]+"\n"+"Horas de apertura: "+B["horario"]["apertura"]+"-"+B["horario"]["cierre"]
            lblHorario.config(text=t)
            NombreBT.config(text=n)
            ingreso.withdraw()
            Ebiblioteca.deiconify()
        else:
            lbltextito.config(text="esa biblioteca no existe")
        limpiarCamposI()
    except:
        alertaT()



ingreso=tk.Toplevel(inicio)

ingreso.title("Ingreso")
ingreso.geometry("600x500")

top=tk.Frame(ingreso,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(ingreso,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
content.columnconfigure(2,weight=1)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)
content.rowconfigure(3,weight=1)

tk.Label(top,text="Ingreso",bg="skyblue",font=("Arial",24)).pack()

#texto y entradas
nombreI=tk.StringVar()
lblNombre = tk.Label(content,text="Nombre:",bg="white")
txtNombre = tk.Entry(content,textvariable=nombreI)


lblNombre.grid(row=0, column=0)
txtNombre.grid(row=0, column=1, columnspan=2)

idI=tk.StringVar()
lblID = tk.Label(content,text="ID:",bg="white")
txtID = tk.Entry(content,textvariable=idI)

lblID.grid(row=1, column=0)
txtID.grid(row=1, column=1, columnspan=2)

lbltextito = tk.Label(content,text="",bg="white")

lbltextito.grid(row=2, column=0, columnspan=3)

btnIngresar = tk.Button(content,text="Ingresar",command=irEbiblioteca1)
btnIngresar.grid(row=3, column=0)

btnSalir = tk.Button(content,text="Salir",command=irInicio2)
btnSalir.grid(row=3, column=2)
ingreso.withdraw()



#opciones de biblioteca

def irLibros1():
    
    Ebiblioteca.withdraw()
    libros.deiconify()
    actualizarL()



    
def irAutores1():
    actualizarA()
    Ebiblioteca.withdraw()
    autores.deiconify()
def irPrestamos1():
    actualizarP()
    Ebiblioteca.withdraw()
    prestamos.deiconify()
def irEhorario1():
    Ebiblioteca.withdraw()
    Ehorario.deiconify()
def irIngreso2():
    Ebiblioteca.withdraw()
    ingreso.deiconify()


Ebiblioteca=tk.Toplevel(inicio)

Ebiblioteca.title("opciones")
Ebiblioteca.geometry("600x500")

top=tk.Frame(Ebiblioteca,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(Ebiblioteca,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
content.columnconfigure(2,weight=1)
content.columnconfigure(3,weight=1)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)



NombreBT=tk.Label(top,text="Biblioteca(poner nombre:v)",bg="skyblue",font=("Arial",24))
NombreBT.pack()

btnLibros = tk.Button(content,text="Libros",command=irLibros1, width=20, font=("Arial",16))
btnLibros.grid(row=0, column=0, columnspan=2)

btnAutores = tk.Button(content,text="Autores",command=irAutores1, width=20, font=("Arial",16))
btnAutores.grid(row=0, column=2, columnspan=2)


btnHorario = tk.Button(content,text="Horario",command=irEhorario1, width=20, font=("Arial",16))
btnHorario.grid(row=1, column=0, columnspan=2)


btnPrestamos = tk.Button(content,text="Prestamos",command=irPrestamos1, width=20, font=("Arial",16))
btnPrestamos.grid(row=1, column=2, columnspan=2)

btnSalir = tk.Button(content,text="Salir",command=irIngreso2, width=20, font=("Arial",16))
btnSalir.grid(row=2, column=1, columnspan=2)

Ebiblioteca.withdraw()



#libros
ISBNL=""

def irEbiblioteca2():
    libros.withdraw()
    Ebiblioteca.deiconify()
def irRegistroL():
    listboxPag2.delete(0, tk.END)
    libros.withdraw()
    registroL.deiconify()
def irElibro1():
    global ISBNL
    try:
        s=listboxL.curselection()[0]
        with open(f"libros{IDB}.bin","r") as f:
            l=json.load(f)
        d=BI.Libro(l[s]["titulo"],l[s]["ISBN"],[])
        NombreLT.config(text=l[s]["titulo"])
        ISBNL=str(l[s]["ISBN"])
        p=d.leer()
        actualizarPg(p)
        libros.withdraw()
        Elibro.deiconify()
    except:
        alertaS()
def actualizarPg(pags):
    listboxPag1.delete(0, tk.END)
    for b in pags:
        c=str(b["nroPagina"])+" "+b["contenido"]
        listboxPag1.insert(tk.END, c)
def eliminarL():
    try:
        s=listboxL.curselection()[0]
        with open(f"libros{IDB}.bin","r") as f:
            l=json.load(f)
        d=BI.Libro(l[s]["titulo"],l[s]["ISBN"],[])
        d.borrarP()
        b=BI.Biblioteca("","","","",IDB)
        
        b.borrarLibro(d)
        
        actualizarL()
    except:
        alertaS()
    
    
    

    


libros=tk.Toplevel(inicio)

libros.title("libros")
libros.geometry("600x500")

top=tk.Frame(libros,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(libros,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
content.columnconfigure(2,weight=1)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)
content.rowconfigure(3,weight=1)



tk.Label(top,text="Libros",bg="skyblue",font=("Arial",24)).pack()

btnRegistrar = tk.Button(content,text="Registrar",command=irRegistroL)
btnRegistrar.grid(row=0, column=0)

btnLeer = tk.Button(content,text="Leer",command=irElibro1)
btnLeer.grid(row=1, column=0)

btnEliminar = tk.Button(content,text="Eliminar",command=eliminarL)
btnEliminar.grid(row=2, column=0)

btnSalir = tk.Button(content,text="Salir",command=irEbiblioteca2)
btnSalir.grid(row=3, column=0)

listboxL= tk.Listbox(content,width=30, height=18, bg="white", font=("Arial",12))
listboxL.grid(row=0, column=1, rowspan=4, columnspan=2)



#listbox.config(heigth=listbox.size())

libros.withdraw()



#leer


def irLibros2():
    Elibro.withdraw()
    libros.deiconify()
def irRegistropag():
    Elibro.withdraw()
    registroPag.deiconify()
def eliminarPg():
    try:
        s=listboxPag1.curselection()[0]
        with open(f"paginas{ISBNL}.bin","r") as f:
            l=json.load(f)
        lib=BI.Libro("",ISBNL,[])
        d=BI.Pagina(l[s]["nroPagina"],l[s]["contenido"])
        lib.borrarPagina(d)
        l=lib.leer()
        
        actualizarPg(l)
    except:
        alertaS()
    
    
    

    
Elibro=tk.Toplevel(inicio)

Elibro.title("leer")
Elibro.geometry("600x500")

top=tk.Frame(Elibro,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(Elibro,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
content.columnconfigure(2,weight=1)

content.rowconfigure(0,weight=4)
content.rowconfigure(1,weight=1)


NombreLT=tk.Label(top,text="TextLabel(cambiar:v)",bg="skyblue",font=("Arial",24))
NombreLT.pack()

listboxPag1= tk.Listbox(content ,width=30, height=18,bg="white", font=("Arial",12))
listboxPag1.grid(row=0, column=0, columnspan=3)



btnAgregar = tk.Button(content,text="Agregar",command=irRegistropag)
btnAgregar.grid(row=1, column=0)

btnEliminar = tk.Button(content,text="Eliminar",command=eliminarPg)
btnEliminar.grid(row=1, column=1)

btnSalir = tk.Button(content,text="Salir",command=irLibros2)
btnSalir.grid(row=1, column=2)

Elibro.withdraw()

#registro de pagina

def irElibro2():
    registroPag.withdraw()
    Elibro.deiconify()
def limpiarCamposPg():
    NumP.set("")
    ContNu.set("")

def registrarPagNu():
    try:
        global ISBNL
        n=int(NumP.get())
        c=ContNu.get()
        p=BI.Pagina(n,c)
        l=BI.Libro("",ISBNL,[])
        l.agregarPagina(p)
        d=l.leer()
        actualizarPg(d)
        limpiarCamposPg()
    except:
        alertaT()
    

registroPag=tk.Toplevel(inicio)

registroPag.title("registro de pagina")
registroPag.geometry("600x500")

top=tk.Frame(registroPag,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(registroPag,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)

tk.Label(top,text="Registro Pagina",bg="skyblue",font=("Arial",24)).pack()

NumP=tk.StringVar()
lblNumero = tk.Label(content,text="Numero:",bg="white")
txtNumero = tk.Entry(content,textvariable=NumP)

lblNumero.grid(row=0, column=0)
txtNumero.grid(row=0, column=1)

ContNu=tk.StringVar()
lblContenido = tk.Label(content,text="Contenido:",bg="white")
txtContenido = tk.Entry(content,textvariable=ContNu)

lblContenido.grid(row=1, column=0)
txtContenido.grid(row=1, column=1)

btnSalir = tk.Button(content,text="Salir",command=irElibro2)
btnSalir.grid(row=2, column=0)

btnAgregar = tk.Button(content,text="Agregar",command=registrarPagNu)
btnAgregar.grid(row=2, column=1)

registroPag.withdraw()




#registro de libros

PAGS=[]

def irLibros3():
    registroL.withdraw()
    libros.deiconify()
def limpiarCamposL():
    idI.set("")
    titulo.set("")
    ISBN.set("")
def registrarL():
    try:
        global PAGS
        global IDB
        ing=idI.get()
        t=titulo.get()
        i=int(ISBN.get())
        s=BI.Libro(t,i,PAGS)
        b=BI.Biblioteca("","","","",IDB)
        b.agregarLibro(s)
        actualizarL()
        PAGS=[]
        limpiarCamposL()
        listboxPag2.delete(0, tk.END)
    except UnboundLocalError as e:
        alertaL()
    except ValueError as e:
        alertaT()

def eliminarPagina():
    try:
        global PAGS
        d=listboxPag2.curselection()[0]
        PAGS.remove(PAGS[d])
        listboxPag2.delete(listboxPag2.curselection())
    except:
        alertaS()

def limpiarOK():
    cont.set("")
def registrarPaginas():
    try:
        global PAGS
        i=cont.get()
        if i=="" :
            raise ValueError
        else:
            PAGS.append(i)
            listboxPag2.insert(tk.END, i)
            limpiarOK()
    except:
        alertaT()
def actualizarL():
    global IDB
    listboxL.delete(0, tk.END)
    with open(f"libros{IDB}.bin","r") as f:
        s=json.load(f)
    for b in s:
        l=b["titulo"]+" "+str(b["ISBN"])
        listboxL.insert(tk.END, l)




registroL=tk.Toplevel(inicio)

registroL.title("registros de libros")
registroL.geometry("600x500")

top=tk.Frame(registroL,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(registroL,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=2)
content.columnconfigure(1,weight=1)
content.columnconfigure(2,weight=2)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)
content.rowconfigure(3,weight=1)
content.rowconfigure(4,weight=2)
content.rowconfigure(5,weight=1)
content.rowconfigure(6,weight=1)


tk.Label(top,text="Registro Libro",bg="skyblue",font=("Arial",24)).pack()

titulo=tk.StringVar()
lblTitulo = tk.Label(content,text="Titulo:",bg="white")
txtTitulo = tk.Entry(content,textvariable=titulo)

lblTitulo.grid(row=0, column=0)
txtTitulo.grid(row=0, column=1, columnspan=2)

ISBN=tk.StringVar()
lblISBN = tk.Label(content,text="ISBN:",bg="white")
txtISBN = tk.Entry(content,textvariable=ISBN)

lblISBN.grid(row=1, column=0)
txtISBN.grid(row=1, column=1, columnspan=2)

cont=tk.StringVar()
lblContSigPag = tk.Label(content,text="Contenido de la siguiente pagina:",bg="white")
txtContSigPag = tk.Entry(content,textvariable=cont)

lblContSigPag.grid(row=2, column=0, columnspan=3)
txtContSigPag.grid(row=3, column=0, columnspan=3)

listboxPag2= tk.Listbox(content,bg="white", font=("Arial",12), height=10,width=30)
listboxPag2.grid(row=4, column=0, columnspan=3)



btnOk = tk.Button(content,text="Ok",command=registrarPaginas)
btnOk.grid(row=3, column=2)

btnEliminar = tk.Button(content,text="Eliminar",command=eliminarPagina)
btnEliminar.grid(row=5, column=0)

btnRegistrar = tk.Button(content,text="Registrar",command=registrarL)
btnRegistrar.grid(row=5, column=2)

btnSalir = tk.Button(content,text="Salir",command=irLibros3)
btnSalir.grid(row=6, column=1)

registroL.withdraw()



#prestamos


def irEbiblioteca3():
    prestamos.withdraw()
    Ebiblioteca.deiconify()
def irRegistroP():
    prestamos.withdraw()
    registroP.deiconify()
def actualizarP():
    global IDB
    listboxP.delete(0, tk.END)
    with open(f"prestamos{IDB}.bin","r") as f:
        s=json.load(f)
    for b in s:
        l=b["estudiante"]["nombre"]+"-"+b["libro"]["titulo"]
        listboxP.insert(tk.END, l)
def eliminarP():
    try:
        s=listboxP.curselection()[0]
        with open(f"prestamos{IDB}.bin","r") as f:
            l=json.load(f)
        lib=BI.Libro(l[s]["libro"]["titulo"],l[s]["libro"]["ISBN"],[])
        est=BI.Estudiante(l[s]["estudiante"]["codigo"],"")
        p=BI.Prestamo(est,lib)
        b=BI.Biblioteca("","","","",IDB)
        b.borrarPrestamo(p)
        
        actualizarP()
    except:
        alertaS()
    
    


prestamos=tk.Toplevel(inicio)

prestamos.title("prestamos")
prestamos.geometry("600x500")

top=tk.Frame(prestamos,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(prestamos,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=2)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)


tk.Label(top,text="Prestamos",bg="skyblue",font=("Arial",24)).pack()

btnRegistrar = tk.Button(content,text="Registrar",command=irRegistroP)
btnRegistrar.grid(row=0, column=0)

btnEliminar = tk.Button(content,text="Eliminar",command=eliminarP)
btnEliminar.grid(row=1, column=0)

btnSalir = tk.Button(content,text="Salir",command=irEbiblioteca3)
btnSalir.grid(row=2, column=0)

listboxP= tk.Listbox(content,width=30, height=18, bg="white", font=("Arial",12))
listboxP.grid(row=0, column=1, rowspan=3)



prestamos.withdraw()




#registro prestamo



def irPrestamos2():
    registroP.withdraw()
    prestamos.deiconify()
def limpiarCamposP():
    NomEst.set("")
    CodEst.set("")
    NomLib.set("")
    ISBNlib.set("")
def registrarP():
    try:
        global IDB
        n=NomEst.get()
        c=CodEst.get()
        ln=NomLib.get()
        Li=int(ISBNlib.get())
        lib=BI.Libro(ln,Li,[])
        est=BI.Estudiante(c,n)
        b=BI.Biblioteca("","","","",IDB)
        b.prestarLibro(est,lib)
        actualizarP()
        limpiarCamposP()
    except:
        alertaT()


registroP=tk.Toplevel(inicio)

registroP.title("Registro de prestamo")
registroP.geometry("600x500")

top=tk.Frame(registroP,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(registroP,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)
content.rowconfigure(3,weight=1)
content.rowconfigure(4,weight=1)
content.rowconfigure(5,weight=1)
content.rowconfigure(6,weight=1)


tk.Label(top,text="Registro de Prestamo",bg="skyblue",font=("Arial",24)).pack()

lblEstudiante = tk.Label(content,text="Estudiante:",bg="white")
lblEstudiante.grid(row=0, column=0, columnspan=2)

NomEst=tk.StringVar()
lblUsuario = tk.Label(content,text="Nombre:",bg="white")
txtUsuario = tk.Entry(content,textvariable=NomEst)

lblUsuario.grid(row=1, column=0)
txtUsuario.grid(row=1, column=1)

CodEst=tk.StringVar()
lblCodigo = tk.Label(content,text="Codigo:",bg="white")
txtCodigo = tk.Entry(content,textvariable=CodEst)

lblCodigo.grid(row=2, column=0)
txtCodigo.grid(row=2, column=1)

lblLibro = tk.Label(content,text="Libro:",bg="white")
lblLibro.grid(row=3, column=0, columnspan=2)

NomLib=tk.StringVar()
lblNombreLibro = tk.Label(content,text="Nombre:",bg="white")
txtNombreLibro = tk.Entry(content,textvariable=NomLib)

lblNombreLibro.grid(row=4, column=0)
txtNombreLibro.grid(row=4, column=1)

ISBNlib=tk.StringVar()
lblISBN = tk.Label(content,text="ISBN:",bg="white")
txtISBN = tk.Entry(content,textvariable=ISBNlib)

lblISBN.grid(row=5, column=0)
txtISBN.grid(row=5, column=1)

btnRegistrar = tk.Button(content,text="Registrar",command=registrarP)
btnRegistrar.grid(row=6, column=0)

btnSalir = tk.Button(content,text="Salir",command=irPrestamos2)
btnSalir.grid(row=6, column=1)

registroP.withdraw()


#mostrar el horario





def irEbiblioteca4():
    Ehorario.withdraw()
    Ebiblioteca.deiconify()




Ehorario=tk.Toplevel(inicio)

Ehorario.title("El horario")
Ehorario.geometry("600x500")

top=tk.Frame(Ehorario,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(Ehorario,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)


tk.Label(top,text="Horario",bg="skyblue",font=("Arial",24)).pack()

lblHorario = tk.Label(content,text="horario no identificado",bg="white")
lblHorario.grid(row=0, column=0, columnspan=2)



btnSalir = tk.Button(content,text="Salir",command=irEbiblioteca4)
btnSalir.grid(row=1, column=1)

Ehorario.withdraw()







#Autotres



def irEbiblioteca5():
    autores.withdraw()
    Ebiblioteca.deiconify()
def irRegistroA():
    autores.withdraw()
    registroA.deiconify()
autores=tk.Toplevel(inicio)
def eliminarA():
    try:
        s=listboxA.curselection()[0]
        with open(f"autores{IDB}.bin","r") as f:
            l=json.load(f)
        b=BI.Biblioteca("","","","",IDB)
        a=BI.Autor(l[s]["Nombre"],l[s]["Nacionalidad"])
        b.borrarAutor(a)
        
        actualizarA()
    except:
        alertaS()


autores.title("Autores")
autores.geometry("600x500")

top=tk.Frame(autores,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(autores,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=2)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)


tk.Label(top,text="Autores",bg="skyblue",font=("Arial",24)).pack()

btnRegistrar = tk.Button(content,text="Registrar",command=irRegistroA)
btnRegistrar.grid(row=0, column=0)

btnEliminar = tk.Button(content,text="Eliminar",command=eliminarA)
btnEliminar.grid(row=1, column=0)

btnSalir = tk.Button(content,text="Salir",command=irEbiblioteca5)
btnSalir.grid(row=2, column=0)

listboxA= tk.Listbox(content, width=30, height=18,bg="white", font=("Arial",12))
listboxA.grid(row=0, column=1, rowspan=3)

autores.withdraw()



#RegistroAutor
def limpiarCamposA():
    nomA.set("")
    nacA.set("")

def registrarA():
    try:
        global IDB
        n=nomA.get()
        na=nacA.get()
        s=BI.Autor(n,na)
        b=BI.Biblioteca("","","","",IDB)
        b.agregarAutor(s)
        actualizarA()
        limpiarCamposA()
    except:
        alertaT()
def actualizarA():
    global IDB
    listboxA.delete(0, tk.END)
    with open(f"autores{IDB}.bin","r") as f:
        s=json.load(f)
    for b in s:
        l=b["Nombre"]+"-"+b["Nacionalidad"]
        listboxA.insert(tk.END, l)




def irAutores2():
    registroA.withdraw()
    autores.deiconify()
registroA=tk.Toplevel(inicio)

registroA.title("registro de autor")
registroA.geometry("600x500")

top=tk.Frame(registroA,bg="skyblue")
top.pack(fill="x")

content=tk.Frame(registroA,bg="white")
content.pack(expand=True,fill="both")
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)

content.rowconfigure(0,weight=1)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=1)


tk.Label(top,text="Registro Autor",bg="skyblue",font=("Arial",24)).pack()

nomA=tk.StringVar()
lblNombre = tk.Label(content,text="Nombre:",bg="white")
txtNombre = tk.Entry(content,textvariable=nomA)

lblNombre.grid(row=0, column=0)
txtNombre.grid(row=0, column=1)

nacA=tk.StringVar()
lblNacionalidad = tk.Label(content,text="Nacionalidad:",bg="white")
txtNacionalidad = tk.Entry(content,textvariable=nacA)

lblNacionalidad.grid(row=1, column=0)
txtNacionalidad.grid(row=1, column=1)

btnSalir = tk.Button(content,text="Salir",command=irAutores2)
btnSalir.grid(row=2, column=0)

btnRegistrar = tk.Button(content,text="Registrar",command=registrarA)
btnRegistrar.grid(row=2, column=1)

registroA.withdraw()

inicio.mainloop()





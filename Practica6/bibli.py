from datetime import date
from datetime import timedelta
import os
import json


class Pagina:
    def __init__(self,NroPag,contPag):
        self.__NroPagina=NroPag
        self.__contPagina=contPag
    def to_dict(self):
        return {
            "nroPagina": self.__NroPagina,
            "contenido": self.__contPagina,
        }
    def getNro(self):
        return self.__NroPagina
    def getContenido(self):
        return self.__contPagina
    def mostrarPagina(self):
        print("Numero de pagina: {} | Contenido de pagina: {}".format(self.__NroPagina,self.__contPagina))

class Estudiante:
    def __init__(self,codEstudiante,nombre):
        self.__codigoEstudiante=codEstudiante
        self.__nombre=nombre
    def to_dict(self):
        return {
            "codigo": self.__codigoEstudiante,
            "nombre": self.__nombre,
        }
    def getCodigo(self):
        return self.__codigoEstudiante
    def getNombre(self):
        return self.__nombre
    def mostrarInfo(self):
        print("Codigo de estudiante: {} | Nombre: {}".format(self.__codigoEstudiante,self.__nombre))

class Autor:
    def __init__(self,nombre,nacionalidad):
        self.__nombre=nombre
        self.__nacionalidad=nacionalidad
    def to_dict(self):
        return {
            "Nombre": self.__nombre,
            "Nacionalidad": self.__nacionalidad,
        }
    def getNombre(self):
        return self.__nombre
    def getNacionalidad(self):
        return self.__nacionalidad
    def mostrarInfo(self):
        print("Nombre: {} | Nacionalidad: {}".format(self.__nombre,self.__nacionalidad))
        
class Libro:
    def __init__(self,titulo,ISBN,contPags):
        self.__titulo=titulo
        self.__ISBN=ISBN
        self.__paginas=f"paginas{ISBN}.bin"
        for e in contPags:
            if os.path.exists(self.__paginas) and os.path.getsize(self.__paginas)>0:
                with open(self.__paginas, "r") as f:
                    lista_pag = json.load(f)
                print(len(lista_pag) )
                num = len(lista_pag) + 1
            else:
                num=1
            self.agregarPagina(Pagina(num,e))
    def agregarPagina(self,pagina):
        pag=pagina.to_dict()
        if os.path.exists(self.__paginas) and os.path.getsize(self.__paginas)>0:
            try:
                with open(self.__paginas,"r")as f:
                    s=json.load(f)
            except:
                s=[]
        else:
            s=[]
        s.append(pag)
        with open(self.__paginas,"w")as f:
                json.dump(s,f,indent=4)
    def borrarPagina(self,pag):
        l=[]
        try:
            with open(self.__paginas,"r")as f:
                s=json.load(f)
            for pagina in s:
                if not pagina["nroPagina"]==pag.getNro():
                    l.append(pagina)
            with open(self.__paginas,"w")as f:
                json.dump(l,f,indent=4)
        except:
            print("algo salio mal")
            
    def borrarP(self):
        s=[]
        with open(self.__paginas,"w")as f:
            json.dump(s,f,indent=4)
            
        
            

    def to_dict(self):
        if os.path.exists(self.__paginas) and os.path.getsize(self.__paginas) > 0:
            with open(self.__paginas, "r") as f:
                lista_pag = json.load(f)
        return {
            "titulo": self.__titulo,
            "ISBN": self.__ISBN,
            "paginas": lista_pag
        }
    def getTitulo(self):
        return self.__titulo
    def getISBN(self):
        return self.__ISBN
    def __str__(self):
        return "Titulo: {} | ISBN: {} ".format(self.__titulo,self.__ISBN)
    def  leer(self):
        if os.path.exists(self.__paginas) and os.path.getsize(self.__paginas) > 0:
            with open(self.__paginas, "r") as f:
                lista_pag = json.load(f)
        return lista_pag
            
class Prestamo:
    def __init__(self,estudiante,libro):
        self.__estudiante=estudiante
        self.__libro=libro
        self.__fechaPrestamo = date.today()
        self.__fechaDevolucion = self.__fechaPrestamo + timedelta(days=7)
    def getLibro(self):
        return self.__libro
    def getEstudiante(self):
        return self.__estudiante
    def to_dict(self):
        return {
            "estudiante": self.__estudiante.to_dict(),
            "libro": self.__libro.to_dict(),
            "fecha de prestamo":self.__fechaPrestamo.strftime("%Y-%m-%d %H:%M:%S"),
            "fecha de devolucion":self.__fechaDevolucion.strftime("%Y-%m-%d %H:%M:%S")
        }
        
    def mostrarInfo(self):
        print("Fecha de prestamo: {} | Fecha de devolucion: {} ".format(self.__fechaPrestamo,self.__fechaDevolucion))
        print("Estudiante:")
        self.__estudiante.mostrarInfo()
        print("Libro:")
        print(self.__libro)
        
class Horario:
    def __init__(self,diasAp,horaAp,horaCi):
        self.__diasApertura=diasAp
        self.__horaApertura=horaAp
        self.__horaCierre=horaCi
    def to_dict(self):
        return{
            "dias":self.__diasApertura,
            "apertura":self.__horaApertura,
            "cierre":self.__horaCierre
            }
    def mostrarHorario(self):
        return "Dias de apertura: {} | Hora de apertura :{} | Hora de cierre : {}".format(self.__diasApertura,self.__horaApertura,self.__horaCierre)
        
class Biblioteca:
    def __init__(self,nombre,diasAp,horaAp,horaCi,ID):
        s=[]
        self.__nombre=nombre
        self.__libros=f"libros{ID}.bin"
        self.__autores=f"autores{ID}.bin"
        self.__prestamos=f"prestamos{ID}.bin"
        self.__horario=Horario(diasAp,horaAp,horaCi)
        self.__ID=ID
        if not os.path.exists(self.__libros) or os.path.getsize(self.__libros)==0:
            with open(self.__libros,"w")as f:
                    json.dump(s,f,indent=4)
        if not os.path.exists(self.__autores) or os.path.getsize(self.__autores)==0:
            with open(self.__autores,"w")as f:
                    json.dump(s,f,indent=4)
        if not os.path.exists(self.__prestamos) or os.path.getsize(self.__prestamos)==0:
            with open(self.__prestamos,"w")as f:
                    json.dump(s,f,indent=4)
    def getID(self):
        return self.__ID
    def getNombre(self):
        return self.__nombre
    
    def agregarLibro(self,libro):
        lib=libro.to_dict()
        if os.path.exists(self.__libros) and os.path.getsize(self.__libros)>0:
            try:
                with open(self.__libros,"r")as f:
                    s=json.load(f)
            except:
                s=[]
        else:
            s=[]
        s.append(lib)
        with open(self.__libros,"w")as f:
                json.dump(s,f,indent=4)
    def mostrarLibros(self):
        try:
            with open(self.__libros,"r")as f:
                s=json.load(f)
            print(s)
        except:
            print("algo salio mal")
            
    def borrarLibro(self,lib):
        l=[]
        try:
            with open(self.__libros,"r")as f:
                s=json.load(f)
            for libro in s:

                if not libro["titulo"]==lib.getTitulo() or not libro["ISBN"]==lib.getISBN():
                    l.append(libro)
            with open(self.__libros,"w")as f:
                json.dump(l,f,indent=4)
        except:
            print("algo salio mal")
    def borrarL(self):
        s=[]
        with open(self.__libros,"w")as f:
            json.dump(s,f,indent=4)
                    
                    
    
        
        
    def agregarAutor(self,autor):
        au=autor.to_dict()
        if os.path.exists(self.__autores) and os.path.getsize(self.__autores)>0:
            try:
                with open(self.__autores,"r")as f:
                    s=json.load(f)
            except:
                s=[]
        else:
            s=[]
        s.append(au)
        with open(self.__autores,"w")as f:
                json.dump(s,f,indent=4)
    def mostrarAutores(self):
        try:
            with open(self.__autores,"r")as f:
                s=json.load(f)
            print(s)
        except:
            print("algo salio mal")
            
    def borrarAutor(self,au):
        l=[]
        try:
            with open(self.__autores,"r")as f:
                s=json.load(f)
            for autor in s:
                if not autor["Nombre"]==au.getNombre() or not autor["Nacionalidad"]==au.getNacionalidad():
                    l.append(autor)
            with open(self.__autores,"w")as f:
                json.dump(l,f,indent=4)
        except:
            print("algo salio mal")
    def borrarA(self):
        s=[]
        with open(self.__autores,"w")as f:
            json.dump(s,f,indent=4)

    def borrarPR(self):
        s=[]
        with open(self.__prestamos,"w")as f:
            json.dump(s,f,indent=4)
                
    def prestarLibro(self,estudiante,lib):
        g=[]
        prestamo=None
        with open(self.__libros,"r")as f:
            l=json.load(f)
        for libro in l:

                if libro["titulo"]==lib.getTitulo() and libro["ISBN"]==lib.getISBN():
                    prestamo=Prestamo(estudiante,lib)
                    lib.borrarP()
                    
                else:
                    g.append(libro)

        with open(self.__libros,"w")as f:
            json.dump(g,f,indent=4)
            
        if prestamo !=None:
            p=prestamo.to_dict()
            if os.path.exists(self.__prestamos) and os.path.getsize(self.__prestamos)>0:

                try:
                    with open(self.__prestamos,"r")as f:
                        s=json.load(f)

                except:
                    s=[]
            else:
                s=[]
            s.append(p)
            with open(self.__prestamos,"w")as f:
                    json.dump(s,f,indent=4)

        else:
            print("no se encontro el libro")
        return self

    def borrarPrestamo(self,pres):
        l=[]
        try:
            with open(self.__prestamos,"r")as f:
                s=json.load(f)
            for prestamo in s:
                if not prestamo["libro"]["titulo"]==pres.getLibro().getTitulo() or not prestamo["estudiante"]["codigo"]==pres.getEstudiante().getCodigo():
                    l.append(prestamo)
                else:
                    self.agregarLibro(pres.getLibro())
            with open(self.__prestamos,"w")as f:
                json.dump(l,f,indent=4)
        except Exception as e:
            print(e)
            
    def mostrarPrestamos(self):
        try:
            with open(self.__prestamos,"r")as f:
                s=json.load(f)
            print(s)
        except:
            print("algo salio mal")
    
        
    
    def to_dict(self):
        with open(self.__libros,"r")as f:
            s=json.load(f)
        with open(self.__autores,"r")as f:
            t=json.load(f)
        with open(self.__prestamos,"r")as f:
            u=json.load(f)
        return{
            "nombre":self.__nombre,
            "libros":s,
            "autores":t,
            "prestamos":u,
            "horario":self.__horario.to_dict(),
            "ID":self.__ID

            }
def agregar(biblioteca):
    bi=biblioteca.to_dict()
    if os.path.exists("general.bin") and os.path.getsize("general.bin")>0:
            try:
                with open("general.bin","r")as f:
                    s=json.load(f)
            except:
                s=[]
    else:
            s=[]
    s.append(bi)
    with open("general.bin","w")as f:
        json.dump(s,f,indent=4)
        

def borrar(bi):
        l=[]
        try:
            with open("general.bin","r")as f:
                s=json.load(f)
            for Bibli in s:
                if not Bibli["ID"]==bi.getID() and not Bibli["nombre"]==bi.getNombre() :
                    l.append(Bibli)
            with open("general.bin","w")as f:
                json.dump(l,f,indent=4)
        except Exception as e:
            print(e)

def buscar(bi):
        l=[]
        a=None
        try:
            with open("general.bin","r")as f:
                s=json.load(f)
            for Bibli in s:
                if  Bibli["ID"]==bi.getID() and Bibli["nombre"]==bi.getNombre() :
                    a=Bibli
        except:
            print("algo salio mal")
        return a




def mostrar():
    with open("general.bin","r")as f:
        s=json.load(f)
    print(s)
def borrarT():
        s=[]
        with open("principal.bin","w")as f:
            json.dump(s,f,indent=4)



    


    
        






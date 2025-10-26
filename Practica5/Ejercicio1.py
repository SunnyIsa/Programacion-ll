from datetime import date
from datetime import timedelta
class Pagina:
    def __init__(self,NroPag,contPag):
        self.__NroPagina=NroPag
        self.__contPagina=contPag
    def mostrarPagina(self):
        print("Numero de pagina: {} | Contenido de pagina: {}".format(self.__NroPagina,self.__contPagina))
class Estudiante:
    def __init__(self,codEstudiante,nombre):
        self.__codigoEstudiante=codEstudiante
        self.__nombre=nombre
    def mostrarInfo(self):
        print("Codigo de estudiante: {} | Nombre: {}".format(self.__codigoEstudiante,self.__nombre))
class Autor:
    def __init__(self,nombre,nacionalidad):
        self.__nombre=nombre
        self.__nacionalidad=nacionalidad
    def mostrarInfo(self):
        print("Nombre: {} | Nacionalidad: {}".format(self.__nombre,self.__nacionalidad))
class Libro:
    def __init__(self,titulo,ISBN,contPags):
        self.__titulo=titulo
        self.__ISBN=ISBN
        self.__paginas=[]
        for i in range(len(contPags)):
            pagina=Pagina(i+1,contPags[i])
            self.__paginas.append(pagina)
    def __str__(self):
        return "Titulo: {} | ISBN: {} ".format(self.__titulo,self.__ISBN)
    def  leer(self):
        for pagina in (self.__paginas):
            pagina.mostrarPagina()
class Prestamo:
    def __init__(self,estudiante,libro):
        self.__estudiante=estudiante
        self.__libro=libro
        self.__fechaPrestamo = date.today()
        self.__fechaDevolucion = self.__fechaPrestamo + timedelta(days=7)
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
    def mostrarHorario(self):
        print("Dias de apertura: {} | Hora de apertura :{} | Hora de cierre : {}".format(self.__diasApertura,self.__horaApertura,self.__horaCierre))
class Biblioteca:
    def __init__(self,nombre,diasAp,horaAp,horaCi):
        self.__nombre=nombre
        self.__libros=[]
        self.__autores=[]
        self.__prestamos=[]
        self.__horario=Horario(diasAp,horaAp,horaCi)
    def agregarLibro(self,libro):
        self.__libros.append(libro)
        return self
    def agregarAutor(self,autor):
        if autor not in self.__autores:
            self.__autores.append(autor)
        return self
    def prestarLibro(self,estudiante,libro):
        if libro in self.__libros:
            prestamo=Prestamo(estudiante,libro)
            self.__prestamos.append(prestamo)
            self.__libros.remove(libro)
        return self
    def mostrarEstado(self):
        if self.__prestamos !=None:
            print("Biblioteca: "+self.__nombre)
            self.__horario.mostrarHorario()
            print("Libros disponibles")
            for libro in self.__libros:
                print(libro)
                libro.leer()
            print("Autores")
            for autor in self.__autores:
                autor.mostrarInfo()
            print ("Prestamos activos")
            for prestamo in self.__prestamos:
                prestamo.mostrarInfo()
        else:
            print("Esta biblioteca esta cerrada")
    def cerrarBiblioteca(self):
        print("La Biblioteca cerro")
        self.__prestamos=None
        
b1= Biblioteca("Municipal La Paz","Lun–Vie","08:00","18:00")
e1= Estudiante("E001", "Ana Pérez")
e2=Estudiante("E002", "Luis Gutiérrez")
e3=Estudiante("E003", "María Fernanda Díaz")
e4=Estudiante("E004", "Jorge Ramírez")
e5=Estudiante("E005", "Sofía Aguilar")
e6=Estudiante("E006", "Carlos Mendoza")

a1=Autor("Gabriel García Márquez", "Colombia")
a2=Autor("Antoine de Saint-Exupéry", "Francia")
a3=Autor("Julio Cortázar", "Argentina")
a4=Autor("Mario Vargas Llosa", "Perú")
a5=Autor("Isabel Allende", "Chile")
a6=Autor("Jorge Luis Borges", "Argentina")

L1=Libro("Cien años de soledad", "978-0307474728",["Macondo amanece", "La estirpe de los Buendía", "Plagas y prodigios"])
L2=Libro("El principito", "978-0156012195", ["Encuentro en el desierto", "Planetas y personajes", "El zorro y el secreto"])
L3=Libro("Rayuela", "978-8437604947", ["Del lado de acá", "Del lado de allá", "Tablero de dirección"])
L4=Libro("La ciudad y los perros", "978-8420471983", ["El Jaguar", "El Esclavo", "El círculo del Colegio Militar"])
L5=Libro("La casa de los espíritus", "978-0553383805", ["La familia Trueba", "Amores y fantasmas", "Destino y memoria"])
L6=Libro("Ficciones", "978-8420633121", ["El jardín de senderos que se bifurcan", "La lotería en Babilonia", "Funes el memorioso"])
b1.agregarLibro(L1)
b1.agregarLibro(L2)
b1.agregarLibro(L3)
b1.agregarLibro(L4)
b1.agregarLibro(L5)
b1.agregarLibro(L6)
b1.agregarAutor(a1)
b1.agregarAutor(a2)
b1.agregarAutor(a3)
b1.agregarAutor(a4)
b1.agregarAutor(a5)
b1.agregarAutor(a6)
b1.mostrarEstado()
print()
b1.prestarLibro(e2,L2)
b1.prestarLibro(e5,L4)
b1.prestarLibro(e3,L5)
b1.mostrarEstado()
print()
b1.cerrarBiblioteca()
b1.mostrarEstado()





            
            
    
        

    
        

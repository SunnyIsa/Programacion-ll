class Persona:
    def __init__(self,nombre,edad,pesoPersona):
        self.__nombre=nombre
        self.__edad=edad
        self.__pesoPersona=pesoPersona
    def getPeso(self):
        return self.__pesoPersona
    def getEdad(self):
        return self.__edad
    def getNombre(self):
        return self.__nombre
class Cabina:
    def __init__(self,nroCabina):
        self.__nroCabina=nroCabina
        self.__personasAbordo=[]
    def agregarPersona(self,p):
        if len(self.__personasAbordo)<11 and self.calcularPeso()<850:
            self.__personasAbordo.append(p)
    def calcularPeso(self):
        s=0
        for i in range(len(self.__personasAbordo)):
            s+=self.__personasAbordo[i].getPeso()
        return s
    def getNro(self):
        return self.__nroCabina
    def verificar(self):
        if len(self.__personasAbordo)<11 and self.calcularPeso()<850:
            return True
    def calcularReg(self):
        s=0
        for i in range(len(self.__personasAbordo)):
            if self.__personasAbordo[i].getEdad>24 and self.__personasAbordo[i].getEdad<61:
                s+=1
        return s
class Linea:
    def __init__(self,color):
        self.__color=color
        self.__filaPersonas=[]
        self.__cabinas=[]
        self.__cantidadCabinas=0
    def agregarPersona(self,p):
        self.__filaPersonas.append(p)
    def agregarCabina(self,nroCab):
        self.__cabinas.append(Cabina(nroCab))
        self.__cantidadCabinas+=1
    def getColor(self):
        return self.__color
    def getNro(self):
        return self.__cantidadCabinas
    def subirPersona(self,X):
        p=self.__filaPersonas[0].getEdad()
        for i in range(self.__cantidadCabinas):
            if self.__cabinas[i].getNro==X:
                self.__cabinas[i].agregarPersona(self.__filaPersonas[0])
                
                self.__filaPersonas.remove(self.__filaPersonas[0])
                break
        if p>24 and p<61:
            return True
    def verificar(self):
        for i in range(len(self.__cantidadCabinas)):
            if not(self.__cabinas[i].verificar()):
                print(self.__cabinas[i].getNro)
                return False
        return True
    def calcularReg(self):
        s=0
        for i in range(self.__cantidadCabinas):
            s+=self.__cabinas[i].calcularReg()
        return s
                
                
            
class MiTeleferico:
    def __init__(self):
        self.__lineas=[]
        self.__cantidadIngresos=0
        self.__lineas.append(Linea("Amarillo"))
        self.__lineas.append(Linea("Rojo"))
        self.__lineas.append(Linea("Verde"))
    def agregarPersonaFila(self,p,linea):
        for i in range(3):
            if self.__lineas[i].getColor()==linea:
                self.__lineas[i].agregarPersona(p)
                break
    def agregarCabina(self,linea):
        for i in range(3):
            if self.__lineas[i].getColor()==linea:
                self.__lineas[i].agregarCabina(self.__lineas[i].getNro()+1)
                break
    def subirPersona(self,l,X):
        for i in range(3):
            if self.__lineas[i].getColor()==l:
                self.__lineas[i].subirPersona(X)
                if self.__lineas[i].subirPersona(X):
                    self.__cantidadIngresos+=3
                else:
                    self.__cantidadIngresos+=1.5
                break
    def verificar(self):
        for i in range (3):
            if self.__lineas[i].verificar:
                print("Linea {}:Todas sus cabinas cumplen con los requisitos".format(self.__lineas[i].getColor()))
            else:
                print("Ese numero de cabina no cumple".format(self.__lineas[i].getColor()))
    def Calcular(self):
        return self.__cantidadIngresos
    def Mayor(self):
        s=0
        p=""
        for i in range(3):
            if self.__lineas[i].calcularReg()>s:
                s=self.__lineas[i].calcularReg()
                p=self.__lineas[i].getColor()
        return p
            
p1=Persona("lu",25,30)
p2=Persona("leandra",25,50)
p3=Persona("leandra",1,50)
p4=Persona("leandra",25,50)
p5=Persona("leandra",25,50)
p6=Persona("leandra",12,50)
p7=Persona("leandra",25,50)
p8=Persona("leandra",3,50)
p9=Persona("leandra",25,50)
p10=Persona("leandra",25,50)
M=MiTeleferico()
M.agregarCabina("Amarillo")
M.agregarCabina("Amarillo")
M.agregarCabina("Amarillo")
M.agregarCabina("Amarillo")
M.agregarCabina("Rojo")
M.agregarCabina("Rojo")
M.agregarCabina("Rojo")
M.agregarCabina("Verde")
M.agregarCabina("Verde")
M.agregarCabina("Verde")
M.agregarCabina("Verde")
M.agregarCabina("Verde")
M.agregarPersonaFila(p1,"Amarillo")
M.agregarPersonaFila(p2,"Amarillo")
M.agregarPersonaFila(p3,"Amarillo")
M.agregarPersonaFila(p4,"Rojo")
M.agregarPersonaFila(p5,"Rojo")
M.agregarPersonaFila(p6,"Rojo")
M.agregarPersonaFila(p7,"Verde")
M.agregarPersonaFila(p8,"Verde")
M.agregarPersonaFila(p9,"Verde")
M.subirPersona("Amarillo",1)
M.subirPersona("Amarillo",2)
M.subirPersona("Verde",1)
M.subirPersona("Rojo",2)
M.verificar()
print(M.Calcular())









        
    

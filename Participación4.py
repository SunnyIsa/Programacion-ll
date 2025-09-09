from multimethod import multimethod

class MiEntero:

    def __init__(self, valor):
        self.valor=valor

    def get(self):
        return self.valor

    @multimethod
    def esPar(self):
        if self.valor%2==0:
            return True
        else:
            return False

    @multimethod
    def esImpar(self):
        if self.valor%2 !=0:
            return True
        else:
            return False

    @multimethod
    def esPrimo(self):
        if self.valor<=1:
            return False
        for i in range(2, self.valor):
            if self.valor%i==0:
                return False
        return True

    @multimethod
    def esPar(self,valor: int):
        if valor%2==0:
            return True
        else:
            return False

    @multimethod
    def esImpar(self,valor: int):
        if valor%2!=0:
            return True
        else:
            return False

    @multimethod
    def esPrimo(self,valor: int):
        if valor <=1:
            return False
        for i in range(2,valor):
            if valor%i==0:
                return False
        return True

    @multimethod
    def esPar(self,v:"MiEntero"):
        return v.get()%2==0

    @multimethod
    def esImpar(self,v:"MiEntero"):
        return v.get()%2!=0

    @multimethod
    def esPrimo(self,v:"MiEntero"):
        return v.esPrimo()

    @multimethod
    def equals(self,n:int):
        return self.valor==n

    @multimethod
    def equals(self,v:"MiEntero"):
        return self.valor==v.get()
    
    @multimethod
    def parseInt(array: list):      
        return int("".join(array))

    @multimethod
    def parseInt(s:str):                
        return int(s)

a=MiEntero(7)
b=MiEntero(10)

print(a.get())     
print(a.esPar())    
print(b.esImpar())    
print(a.esPrimo())       

print(a.esPar(8))            
print(a.esImpar(9))           
print(a.esPrimo(11))           

print(a.esPar(b))              
print(b.esPrimo(a))            

print(a.equals(7))             
print(a.equals(b))             

print(MiEntero.parseInt("5678"))          
print(MiEntero.parseInt(['1','2','3']))   

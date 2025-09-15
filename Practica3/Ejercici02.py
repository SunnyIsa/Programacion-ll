import random
class Juego:
    def __init__(self,numeroDeVidas=0,record=0):
        self.numeroDeVidas=numeroDeVidas
        self.original=numeroDeVidas
        self.record=record
    def reiniciaPartida(self):
        self.numeroDeVidas=self.original
        self.record=0
        return self
    def actualizaRecord(self):
        self.record+=1
        return self
    def quitaVida(self):
        self.numeroDeVidas-=1
        return self.numeroDeVidas>0
class JuegoAdivinaNumero(Juego):
    def __init__(self,numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar=0
    def validaNumero(self,x):
        return x>-1 and x<11
    def getRandom(self):
        return random.randint(0,10)
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar=self.getRandom()
        while True:
            num=int(input("Adivina el numero entre 0 y 10: "))
            if self.validaNumero(num):
                if num==self.numeroAAdivinar:
                    print("Acertaste!!")
                    self.actualizaRecord()
                    return self
                elif self.quitaVida():
                    if num>self.numeroAAdivinar:
                        print("el numero es menor ,intenta de nuevo")
                    else:
                        print("el numero es mayor ,intenta de nuevo")
                else:
                    return self
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self,x):
        if not(x>-1 and x<11 and x%2==0):
            print("Error")
        return x>-1 and x<11 and x%2==0
    def getRandom(self):
        return 2*random.randint(0,5)
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self,x):
        if not(x>-1 and x<11 and x%2!=0):
            print("Error")
        return x>-1 and x<11 and x%2!=0
    def getRandom(self):
        return 2*random.randint(0,4)+1
    
print("Adivina Numero")
juego1=JuegoAdivinaNumero(3)
juego1.juega()
print("Adivina Numero Par")
juego2=JuegoAdivinaPar(3)
juego2.juega()
print("Adivina Numero Impar")
juego3=JuegoAdivinaImpar(3)
juego3.juega()
            

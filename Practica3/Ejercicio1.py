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
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar=random.randint(0,10)
        while True:
            num=int(input("Adivina el numero entre 0 y 10: "))
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
juego=JuegoAdivinaNumero(4)
juego.juega()
juego.juega()


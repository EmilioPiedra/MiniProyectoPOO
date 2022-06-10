from asyncio import run

from pip import main
class Jugador:
    def __init__(self,nombre,numero,posicion) :
        self.nombre=nombre
        self.numero=numero
        self.posicion=posicion
        
    def getnombre(self):
        return self._nombre
    
    def setnombre(self,nombre):
        self.nombre=nombre
        
    def getnumero(self):
        return self._numero
    
    def setnumero(self,numero):
        self.numero=numero

    def getposicion(self):
        return self._posicion

    def setposicion (self,posicion):
        self.posicion=posicion

p1 = Jugador ("Nombre",14,"Base")

if __name__ == "__main__":
p1.getnombre ()
p1.getnumero()
p1.getposicion()
        

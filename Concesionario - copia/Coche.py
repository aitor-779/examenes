from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self , marca , modelo , matricula , numeroPuertas):
        super().__init__(marca, modelo, matricula)
        self._numeroPuertas = int(numeroPuertas)
        
    def get_numeroPuertas(self):
        return self._numeroPuertas
        

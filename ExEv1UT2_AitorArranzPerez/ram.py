from componente import Componente

class RAM(Componente):
	def __init__(self,marca,capacidad):
		super().__init__(marca)
		self.capacidad=float(capacidad)


	def getCapacidad(self):
		return self.capacidad

	def calculaPrecioRAM(self):
		precioRAM=self.capacidad*5
		return precioRAM
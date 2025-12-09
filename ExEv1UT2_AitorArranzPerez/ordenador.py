from componente import Componente
class Ordenador:
	def __init__(self,marcaCPU,frecuenciaCPU,marcaRAM,capacidadRAM):
		self.marcaCPU=marcaCPU
		self.frecuenciaCPU=float(frecuenciaCPU)
		self.marcaRAM=marcaRAM
		self.capacidadRAM=float(capacidadRAM)


	def getMarcaCPU(self):
		return self.marcaCPU

	def getFrecuenciaCPU(self):
		return self.frecuenciaCPU

	def getMarcaRAM(self):
		return self.marcaRam

	def getCapacidadRAM(self):
		return self.capacidadRAM
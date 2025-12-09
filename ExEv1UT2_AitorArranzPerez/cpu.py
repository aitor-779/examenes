from componente import Componente

class CPU(Componente):
	def __init__(self,marca,frecuencia):
		super().__init__(marca)
		self.frecuencia=float(frecuencia)


	def getFrecuencia(self):
		return self.frecuencia

	def calculaPrecioCPU(self):
		precioCPU=self.frecuencia*75
		return precioCPU


class InterfazES:
	
	def __init__(self):
		pass
	
	def pedir(self,info):
		return input(info)
	
	def mostrar(self,info):
		print(info)
	
	def pedirDatosOrdenador(self):
		marcaCPU=self.pedir("marcaCPU: ")
		frecuenciaCPU=self.pedir("frecuenciaCPU (en GHz): ")
		marcaRAM=self.pedir("marcaRAM: ")
		capacidadRAM=self.pedir("capacidadRAM (en GB): ")
		return marcaCPU,frecuenciaCPU,marcaRAM,capacidadRAM

	def mostrarDatosOrdenador(self,marcaCPU,frecuenciaCPU,marcaRAM,capacidadRAM):
		self.mostrar("marca CPU: "+marcaCPU)
		self.mostrar("frecuencia CPU: "+str(frecuenciaCPU))
		self.mostrar("marca RAM: "+marcaRAM)
		self.mostrar("capacidad RAM: "+str(capacidadRAM))
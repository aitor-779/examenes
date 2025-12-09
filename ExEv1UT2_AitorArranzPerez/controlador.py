from Vista.interfazES import InterfazES
from ordenador import Ordenador
from componente import Componente
from cpu import CPU
from ram import RAM


class Controlador:
	
	@staticmethod
	def start():
		ies=InterfazES()
		
		#------------------------------------------
		#Pedir al usuario los datos de un ordenador
		
		marcaCPU,frecuenciaCPU,marcaRAM,capacidadRAM = ies.pedirDatosOrdenador()

		#------------------------------------------
		#Construir un objeto Ordenador.

		pc= Ordenador(marcaCPU,frecuenciaCPU,marcaRAM,capacidadRAM)

		#-------------------------------------------------
		#Mostrar los datos del objeto Ordenador construido

		ies.mostrarDatosOrdenador(pc.getMarcaCPU(),pc.getFrecuenciaCPU(),pc.getMarcaRAM(),pc.getCapacidadRAM())


class Pagina():
	def __init__(self,numeroPagina):
		self._numeroPagina = numeroPagina
		self._lineas = list()


	def anadirLinea(self,linea):
		self._lineas.append(linea)

	def getNumeroPagina(self):
		return self._numeroPagina

	def getLineas(self):
		out=""
		for l in self._lineas:
			out=out+l
		return out
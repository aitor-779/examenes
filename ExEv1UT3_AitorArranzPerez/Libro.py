from Pagina import Pagina

class Libro():
	def __init__(self,autor,titulo):
		self._autor = autor
		self._titulo = titulo
		self._paginas = []
		self._cont = -1


	def anadirPagina(self,num):
		self._cont+=1
		self._paginas.append(Pagina(num))		


	def anadirLinea(self,linea):
		self._paginas[self._cont].anadirLinea(linea)


	def getPagina(self,num):
		if(int(num)<1 or int(num)>self._cont):
			return "PAGINA NO ENCONTRADA"
		return self._paginas[num-1].getLineas()

	def getNumeroDePaginas(self):
		return self._cont+1
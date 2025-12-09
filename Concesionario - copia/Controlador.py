from InterfazES import InterfazES
from Matricula import Matricula
from Vehiculo import Vehiculo
from Coche import Coche

class Controlador:
    def __init__(self):
        pass

    @staticmethod
    def start():
        ies=InterfazES()
        matr=Matricula()
        vehi=Vehiculo()
        coch=Coche()
        
        #2.1 Pedir al usuario los datos de un vehículo.
        #escribe el código aquí:
        marca=ies.pedir()
        modelo=ies.pedir()
        matricula=ies.pedir()
       
        
        #2.2 Construir un objeto vehículo
        #escribe el código aquí:
        vehi=Vehiculo(marca,modelo,matricula)


        #2.3 Mostrar por pantalla los datos del vehículo construido
        #escribe el código aquí:
        ies.mostrar(f"{vehi.get_marca()}{vehi.get_modelo()}{vehi.get_matricula}")


        #5.1 Pedir al usuario los datos de un coche.
        #escribe el código aquí:
        marca=ies.pedir()
        modelo=ies.pedir()
        matricula=ies.pedir()
        numeroPuertas=int(ies.pedir())

        #5.2 Construir un objeto coche.
        #escribe el código aquí:
        coch=Coche(marca,modelo,matricula,numeroPuertas)

        #5.3 Repetir lo pedido en 5.1 y 5.2 dos veces más
        #escribe el código aquí:
        marca1=ies.pedir()
        modelo1=ies.pedir()
        matricula1=ies.pedir()
        numeroPuertas1=int(ies.pedir())
        coch=Coche(marca1,modelo1,matricula1,numeroPuertas1)
        marca2=ies.pedir()
        modelo2=ies.pedir()
        matricula2=ies.pedir()
        numeroPuertas2=int(ies.pedir())
        coch=Coche(marca2,modelo2,matricula2,numeroPuertas2)


        #5.4 Mostrar por pantalla los datos de los objetos coche construidos, incluyendo su tasación. 
        #escribe el código aquí:
      
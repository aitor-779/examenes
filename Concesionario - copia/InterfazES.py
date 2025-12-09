
class InterfazES:
    def __init__(self):
        pass

    def mostrar(self,info):
        print(info)

    def pedir(self,info):
        return(input(info))

    def pedirDatosVehiculo(self):
        self.mostrar("Petición de datos del vehículo")
        mar=self.pedir("Marca: ")
        mod=self.pedir("Modelo: ")
        mat=self.pedir("Maticula: ")
        anyo=self.pedir("Año de matriculación: ")
        pre=self.pedir("Precio de matriculación: ")
        return mar,mod,mat,anyo,pre

    def mostrarDatosVehiculo(self,mar,mod,mat,anyo,pre):
        self.mostrar("Muestra de datos del vehículo")
        self.mostrar("Marca: "+str(mar))
        self.mostrar("Modelo: "+str(mod))
        self.mostrar("Maticula: "+str(mat))
        self.mostrar("Año de matriculación: "+str(anyo))
        self.mostrar("Precio de matriculación: "+str(pre))
        
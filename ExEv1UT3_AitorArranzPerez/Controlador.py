
from InterfazES import InterfazES
from Libro import Libro

class Controlador:
    def __init__(self):
        pass

    @staticmethod
    def start():
        ies=InterfazES()

        #--------------------------------------------------------------------------
        #EJERCICIO 1

        #SELECCION DEL LIBRO        
        autor="Anonimo"
        titulo="Ejemplo" 
        libroFileName=autor+" - "+titulo+".txt"       
        
        #COMPROBAR SI EL FICHERO CON EL NOMBRE DADO EXISTE
        #(Si no existe se mostrará un mensaje al usuario y el programa finalizará)
        #Escribir código aquí
        if (libroFileName!="Anonimo - Ejemplo.txt"):
            ies.mostrar("Ese libro no se encuentra")
            quit()

        #ABRIR DEL FICHERO EN MODO LECTURA
        #Escribir código aquí
        f = open(libroFileName, "r", encoding="utf-8")

        #CREACIÓN DEL OBJETO LIBRO
        libro=Libro(autor,titulo)

        #LEER EL FICHERO Y AÑADIR PAGINAS (Y SUS LÍNEAS) AL OBJETO LIBRO
        #Escribir código aquí
        for i in range(1,3):
            libro.anadirPagina(i)
            for i in range(1,9):
                libro.anadirLinea(i)


        #MOSTRAR TODO EL CONTENIDO DEL FICHERO
        #Escribir código aquí

        #ies.mostrar(getPagina(getNumeroDePaginas()))
        

        #CIERRE DEL FICHERO
        #Escribir código aquí
        f.close()

        #MOSTRAR PAGINA DEL LIBRO
        paginaAmostrar=ies.pedir("Página del libro que quieres ver: ")
        ies.mostrar(libro.getPagina(paginaAmostrar))

        #ABRIR EL FICHERO EN MODO AÑADIR
        #Escribir código aquí
        f=open(libroFileName, "w", encoding="utf-8")

        #PEDIR UNA ÚLTIMA LINEA
        ultimaLinea=ies.pedir("Escribe una linea para ser escrita al final del fichero del libro")
        libro.anadirLinea(ultimaLinea)

        #AÑADIR UNA ÚLTIMA LINEA AL FICHERO


        #CIERRE DEL FICHERO
        f.close()

        #--------------------------------------------------------------------------
        #EJERCICIO 2

        #EJERCICIO 2.1
        #Escribir código aquí
        

        #EJERCICIO 2.2
        #Escribir código aquí
        

        #EJERCICIO 2.3
        #Escribir código aquí

        
        
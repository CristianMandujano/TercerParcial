
'''
manejo de archivos de texto
Apertura de archivos
   open("archivo.txt","r")
        
Modos principales
Modo descripción
r leer 
w escribir (sobreescribe)    
a Agregar
x Crear archivo   

***** Lectura de archivos 
*archivo.read()
*archivo.readline()
*archivo.readlines()

***** Escritura de archivos 
*archivo.write("Texto a escribir")
*archivo.writelines(["Linea1\n", "Linea2\n"])
   
'''


def crear_archivo():
    nombre=input("Nombre del archivo: ")
    with open(nombre, "w") as archivo:
        print("Archivo creado correctamente")

crear_archivo()




import os
import os
 
#***** Crear archivo *****
def crear_archivo():
    nombre = input("Nombre del Archivo: ")
    with open(nombre, "w") as archivo: #Mande llamar el archivo cuando abre el archivo y dejas de usarlo lo cierra, with cierra el archivo para quitar el espacio en la ram  
        print ("Archivo creado correctamente")
       
 

#***** agregar datos al archivo *****
def escribir_archivo():
    nombre = input("Nombre del archivo: ")
    texto = input("Escribe el texto a guardar: ")
   
    with open(nombre, "w") as archivo:
        archivo.write(texto)
       
    print("Texto guardado correctamente")
   
 
#***** Escribir Archivo *****
def agregar_texto():
    nombre = input("Nombre del archivo: ")
    texto = input("Texto a agregar: ")
   
    with open(nombre, "a") as archivo:
        archivo.write("\n" + texto)
       
    print("Texto agregado correctamente")


#***** Leer datos del archivo *****
def leer_texto():
    #nombre = input("Nombre del Archivo")
    nombre = "prueba1.txt"
   
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            os.system("cls")
            print("\nContenido del Archivo: ")
            print(contenido)
            print("-------------------------")
            archivo.seek(0) #Donde posicionar para empezar a leer
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")
       
 
def leer_archivo():
    #nombre = input("Nombre del Archivo")
    nombre = "prueba1.txt"
   
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.readlines()
            os.system("cls")
            print("\nContenido del Archivo: ")
            print(contenido)
           
            for linea in contenido:
                print(linea.strip())
               
    except FileNotFoundError:
        print("El archivo no existe")
       
 
def buscar_palabra():
    nombre = input("Nombre del archivo: ")
    palabra = input("Palabra a buscar: ")
   
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
           
        if palabra in contenido:
            print("La palara fue encontrada: ")
        else:
            print("La palabra no se encuentra en el archivo")
    except FileExistsError:
        print("El archivo no existe")
       
 
def menu():
    while True:
        print("\n--- GESTOR DE ARCHIVOS ---")
        print("1. Crear Archivo")
        print("2. Escribir en Archivo")
        print("3. Agregar Texto")
        print("4. Leer Archivo")
        print("5. Buscar Palabra")
        print("6. Salir")
       
        opcion = input("Seleccione una opcion: ")
       
        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            escribir_archivo()
        elif opcion == "3":
            agregar_texto()
        elif opcion == "4":
            leer_archivo()
        elif opcion == "5":
            buscar_palabra()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion Invalida")
           
menu()
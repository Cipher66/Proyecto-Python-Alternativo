import vehiculos_objetos as vo
import vehiculos_clase as vc
import dlc_objetos as dlco
import dlc_clase as dlcl

print("Bienvenido a la aplicacion de ArmA III")
print("¿Que quieres hacer?")
print("1. Ver vehiculos")
print("2. Ver personajes")
print("3. Ver DLC's")

opcion = input("Escribe tu opcion: ")

if opcion == "1":
    for i in vo.lista_vehiculos.lista:
        print(i)
    opcion_añadir = input("¿Quieres añadir un vehiculo?: ")
    if opcion_añadir == "si":
        nombre = input("Nombre del vehiculo: ")
        vo.lista_vehiculos.lista.append(nombre)
        faccion = input("Faccion del vehiculo: ")
        vo.lista_vehiculos.lista.append(faccion)
        tipo = input("Tipo de vehiculo: ")
        vo.lista_vehiculos.lista.append(tipo)
        filename="historial.txt"
        with open("historial.txt", "a") as myfile:
            myfile.write("\nNombre: "+nombre+" facción: "+faccion+" tipo: "+tipo)
    for i in vo.lista_vehiculos.lista:
        print(i)
    if opcion_añadir == "no":
        for i in vo.lista_vehiculos.lista:
            print(i)

if opcion == "3":
    for i in dlco.lista_expansion.lista:
        print(i)
    opcionBus = input("¿Quieres filtrar la busqueda? ")
    if opcionBus == "si":
        opcionFil = input("Palabra clave: ")
        print(str.find(opcionFil))
        
"""
Si el find es mayor que cero, imprimir el objeto correspondiente
"""
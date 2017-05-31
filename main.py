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
        faccion = input("Faccion del vehiculo: ")
        tipo = input("Tipo de vehiculo: ")
        vo.lista_vehiculos.lista.append(vc.Vehiculo(nombre, faccion, tipo))
        filename="historial.txt"
        with open("historial.txt", "a") as myfile:
            myfile.write("Nombre: "+nombre+" facción: "+faccion+" tipo: "+tipo+"\n")
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

        for i in dlco.lista_expansion.lista:
            if i.nombre.upper().find(opcionFil.upper())>= 0:
                print(i)



        """
        def buscar():
            for i in dlco.lista_expansion.lista:
                if i.nombre.find(opcionFil)>=0:
                    return(i)
        
            print(buscar())
        """
        
        #print(opcionFil.find(str(dlco.lista_expansion.lista)))opcionFil
"""
Crear un archivo con los objetos y añadirlos a peticion del usuario y añadirlos a la lista
append.Vehiculo(__, __, __)  

"""

"""
for i in range(len(dlco.lista_expansion.lista)):
if dlco.lista_expansion.lista[i] == opcionFil:
print (dlco.lista_expansion.lista[i])
"""
"""for i in dlco.lista_expansion.lista:
print(i.index(opcionFil))
#print(dlco.lista_expansion.lista.find(opcionFil))
#print(str.find(opcionFil))
"""        
"""
Si el find es mayor que cero, imprimir el objeto correspondiente
a = A("uno")
if a.name.find("u") > 0:
    return a
"""
import vehiculos_clase as vc

""" Antiaéreo """
#my_vehicle_SPAAG = 

"""" Artillería """
#my_vehicle_SPG = 

""" Aviones """
#my_vehicle_Fighter = 

""" Coches """
#my_vehicle_Car = 

""" Drones """
#my_vehicle_Drone = 

""" Helicópteros """
#my_vehicle_Helo = 

""" Tanques """
#my_vehicle_MBT = 

""" Vehiculo de personal """
#my_vehicle_PV = 

lista_vehiculos = vc.listaVehiculos()

lista_vehiculos.addVehiculo(vc.Vehiculo("IFV-6a 'Cheetah'", "OTAN", "Antiaereo"))
lista_vehiculos.addVehiculo(vc.Vehiculo("2S9 'Sochor'", "CSAT", "Artilleria"))
lista_vehiculos.addVehiculo(vc.Vehiculo("A-149 'Gryphon'", "AAF", "Avion"))
lista_vehiculos.addVehiculo(vc.Vehiculo("Hunter", "OTAN", "Coche"))
lista_vehiculos.addVehiculo(vc.Vehiculo("KH-3A 'Fenguang'", "CSAT", "Dron"))
lista_vehiculos.addVehiculo(vc.Vehiculo("CH-49 'Mohawk'", "AAF", "Helicoptero"))
lista_vehiculos.addVehiculo(vc.Vehiculo("M2A1 'Slammer'", "OTAN", "Carro de combate"))
lista_vehiculos.addVehiculo(vc.Vehiculo("MSE-3 'Marid'", "CSAT", "Vehiculo de personal"))



"""
def vehiculos_for():
    for i in vehicles:
        print(i)
    return (i)
    #return str(i)
    #for i in vehicles:
        #return i

print(vehiculos_for())
"""
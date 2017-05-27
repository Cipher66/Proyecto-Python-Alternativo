import vehiculos_clase as vc

""" Antiaéreo """
my_vehicle_SPAAG = vc.Vehiculo("IFV-6a 'Cheetah'", "OTAN", "Antiaereo")

"""" Artillería """
my_vehicle_SPG = vc.Vehiculo("2S9 'Sochor'", "CSAT", "Artilleria")

""" Aviones """
my_vehicle_Fighter = vc.Vehiculo("A-149 'Gryphon'", "AAF", "Avion")

""" Coches """
my_vehicle_Car = vc.Vehiculo("Hunter", "OTAN", "Coche")

""" Drones """
my_vehicle_Drone = vc.Vehiculo("KH-3A 'Fenguang'", "CSAT", "Dron")

""" Helicópteros """
my_vehicle_Helo = vc.Vehiculo("CH-49 'Mohawk'", "AAF", "Helicoptero")

""" Tanques """
my_vehicle_MBT = vc.Vehiculo("M2A1 'Slammer'", "OTAN", "Carro de combate")

""" Vehiculo de personal """
my_vehicle_PV = vc.Vehiculo("MSE-3 'Marid'", "CSAT", "Vehiculo de personal")


vehicles = [my_vehicle_SPAAG, 
            my_vehicle_SPG, 
            my_vehicle_Fighter, 
            my_vehicle_Car, 
            my_vehicle_Drone, 
            my_vehicle_Helo, 
            my_vehicle_MBT, 
            my_vehicle_PV]


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
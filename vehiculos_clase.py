class Vehiculo():
    def __init__(self, nombre, faccion, tipo):
        self.nombre = nombre
        self.faccion = faccion
        self.tipo = tipo
    
    def __str__(self):
        return "Nombre: %s, faccion: %s, tipo: %s" % (self.nombre, self.faccion, self.tipo)

class listaVehiculos():
    def __init__(self):
        self.lista = []
        
    def addVehiculo(self, Vehiculo):
        self.lista.append(Vehiculo)
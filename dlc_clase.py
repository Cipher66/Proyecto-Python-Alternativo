class expansion():
    def __init__(self, nombre, fecha_salida):
        self.nombre = nombre
        self.fecha_salida = fecha_salida
    
    def __str__(self):
        return "Nombre: %s, fecha de salida: %s" % (self.nombre, self.fecha_salida)
class listaExpansion():
    def __init__(self):
        self.lista = []

    def addExpansion(self, expansion):
        self.lista.append(expansion)

               
        
  
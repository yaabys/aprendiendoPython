class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def calcularArea(self):
        return self.lado * self.lado
    
    def type(self):
        return "cuadrado"
class Triangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2
    
    def type(self):
        return "triangulo"
"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

from clases.Cuadrado import Cuadrado
from clases.Triangulo import Triangulo
from clases.Rectangulo import Rectangulo

def calcularArea(poligono):
    area = 0
    if isinstance(poligono, Cuadrado):
        area = poligono.calcularArea()
        print ("El area del " + poligono.type() + " es " + str(area))
    elif isinstance(poligono, Triangulo):
        area = poligono.calcularArea()
        print ("El area del " + poligono.type() + " es " + str(area))
    elif isinstance(poligono, Rectangulo):
        area = poligono.calcularArea()
        print ("El area del " + poligono.type() + " es " + str(area))       
    else:
        print("No es un tipo de poligono!") 

cuadrado = Cuadrado(2)
triangulo = Triangulo(10,5)
rectangulo = Rectangulo(10,5)

calcularArea(cuadrado)
calcularArea(triangulo)
calcularArea(rectangulo)
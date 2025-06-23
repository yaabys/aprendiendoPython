"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

def invertirCadena(cadena):
    # esto es como un split de caracteres como lo casteas a lista directamente
    cadenaSeparada = list(cadena)
    cadenaFinal = ""
    
    for i in reversed(cadenaSeparada):
        cadenaFinal += i
        
    print(cadenaFinal) 
        
invertirCadena("Hola mundo")
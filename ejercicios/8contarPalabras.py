"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""

def contarPalabras(frase):
    listaPalabras = {}
    palabrasSeparadas = frase.split()
    
    for palabra in palabrasSeparadas:
        estaYa = False

        for clave in listaPalabras:
            if palabra == clave:
                listaPalabras[clave] += 1
                estaYa = True
                break

        if not estaYa:
            listaPalabras[palabra] = 1

    print(listaPalabras)
                            
contarPalabras("hola que tal estamos todos y mira todos juntos estamos hola")
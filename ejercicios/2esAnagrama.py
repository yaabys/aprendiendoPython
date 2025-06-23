"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def esAnagrama(palabra1,palabra2):
    if palabra1.lower() == palabra2.lower():
        print("No son anagrama")
    
    palabra1 = "".join(sorted(palabra1.lower().replace(" ", "")))
    palabra2 = "".join(sorted(palabra2.lower().replace(" ", "")))
    if palabra1 == palabra2:
        print("Son anagramas")
    else:
        print("No son anagramas")
        
esAnagrama("hola","aloh")
esAnagrama("hola", "aloh")
esAnagrama("raty", "fairy tales")
esAnagrama("hola", "holaa")
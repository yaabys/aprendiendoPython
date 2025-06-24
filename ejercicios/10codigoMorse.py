"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""

def traductorMorse(texto):
    morse_dict = {
        'a': '.-',     'b': '-...',   'c': '-.-.',   'd': '-..',
        'e': '.',      'f': '..-.',   'g': '--.',    'h': '....',
        'i': '..',     'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',    'p': '.--.',
        'q': '--.-',   'r': '.-.',    's': '...',    't': '-',
        'u': '..-',    'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
        '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
        '8': '---..',  '9': '----.'
    }

    # Diccionario inverso para traducir de Morse a texto
    texto_dict = {v: k for k, v in morse_dict.items()}

    texto = texto.lower().strip()

    # Si empieza con punto o guion, interpretamos como morse
    if texto[0] in ['.', '-']:
        palabras = texto.split(' / ')
        resultado = []
        for palabra in palabras:
            letras = palabra.split()
            traducido = ''.join(texto_dict.get(letra, '?') for letra in letras)
            resultado.append(traducido)
        return ' '.join(resultado)

    else:
        # Es texto normal
        resultado = []
        for palabra in texto.split():
            morse_palabra = ' '.join(morse_dict.get(letra, '?') for letra in palabra)
            resultado.append(morse_palabra)
        return ' / '.join(resultado)

print(traductorMorse("hola mundo"))
# Output: .... --- .-.. .- / -- ..- -. -.. ---

print(traductorMorse(".... --- .-.. .- / -- ..- -. -.. ---"))
# Output: hola mundo        
"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
 * o Trato" y un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 * - En caso contrario retornará un error.
 */
"""

def trucoTrato(nombre,edad,altura,eleccion):
    if eleccion.lower() == truco:
        #comprobar si es par la longitud del nombre si no lo es habria que ir saltando de 2 en 2 en un for 
    elif eleccion.lower() == trato:
        
    else:
        print("No se ha introducido ni truco ni trato")
    

nombre = input("¿Cual es tu nombre?: ")
edad = input("¿Cuantos años tienes?: ")
altura = input("¿Cuanto mides en cm?: ")
eleccion = input("¿Truco o Trato?: ")

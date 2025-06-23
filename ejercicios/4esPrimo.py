"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

lista = []

for i in range(2, 101):
    es_primo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        lista.append(i)

print(lista)

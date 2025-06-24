"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""

def decimalBinario(numeroDecimal):
    
    binario = []
    
    while(numeroDecimal >= 1):
        binario.insert(0,numeroDecimal%2)
        numeroDecimal = numeroDecimal // 2
    
    print(binario)

decimalBinario(123)

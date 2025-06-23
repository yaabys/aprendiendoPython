"""
https://retosdeprogramacion.com/ejercicios/

/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://github.com/yaabys.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
"""

import urllib.request
from PIL import Image
from io import BytesIO

def calcularAspectRatio(link):
    with urllib.request.urlopen(link) as response:
        data = response.read()

    image = Image.open(BytesIO(data))

    width, height = image.size

    print(f"La resolución de la imagen es: {width}x{height}")
    print(f"Aspect ratio (ancho/alto): {width / height:.2f}")

calcularAspectRatio("https://github.com/yaabys.png")

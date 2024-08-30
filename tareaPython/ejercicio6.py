import random

frase = input("Ingresa una frase: ")
vocal = input("ingresa una vocal: ")
posicion = random.randint(0, len(frase))

texto_modificado = frase[:posicion] + vocal.upper() + frase[posicion:]

print(texto_modificado)
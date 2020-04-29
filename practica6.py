texto = input("Mensaje a cifrar: ").lower()
key = int(input("Número de desplazamiento: "))
abecedario = "abcdefghijklmnñopqrstuvwxyz"
cifrado = ""

for l in texto:
    if l in abecedario:
        posicion = abecedario.index(l)
        nueva = (posicion + key) % len(abecedario)
        cifrado+= abecedario[nueva]

def cifracesar(texto,key):
    return cifrado

final = cifracesar(texto,key)
print("Mensaje cifrado:", final)

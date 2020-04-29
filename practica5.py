mensaje = input("Mensaje a cifrar: ").lower()
numero = int(input("Número de desplazamiento: "))
abecedario = "abcdefghijklmnñopqrstuvwxyz"
cifrado = ""

for l in mensaje:
    if l in abecedario:
        posicion = abecedario.index(l)
        nueva = (posicion + numero) % len(abecedario)
        cifrado+= abecedario[nueva]

print("Texto cifrado:", cifrado)

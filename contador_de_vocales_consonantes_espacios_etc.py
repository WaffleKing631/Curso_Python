frase_usuario = input("introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]
espacios = [" "]
comas = [","]
puntos = ["."]

n_vocales = 0
n_consonantes = 0
n_espacios = 0
n_comas = 0
n_puntos = 0
c_letras = []

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    if letra in espacios:
        n_espacios += 1
    if letra in comas:
        n_comas += 1
    if letra in puntos:
        n_puntos += 1
    if letra in vocales:
        c_letras.append(letra)
    else:
        n_consonantes += 1

print("las vocales son {}".format(n_vocales))
print("las consonantes son {}".format(n_consonantes))
print("las comas son {}".format(n_comas))
print("las puntos son {}".format(n_puntos))
print("los espacios son {}".format(n_espacios))
print(c_letras)

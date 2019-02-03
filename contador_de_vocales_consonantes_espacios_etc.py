frase_usuario = input("introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]
espacios = [" "]
comas = [","]
puntos = ["."]
mayusculas = ["A", "B", "C", "D", "E", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "S", "F", "G", "H", "J",
              "K", "L", "Z", "X", "V", "N", "M"]
consonantes = ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z",
               "x", "c", "v", "b", "n", "m", "B", "C", "D", "Q", "W", "R", "T", "Y", "P",
               "S", "F", "G", "H", "J", "K", "L", "Z", "X", "V", "N", "M"]

n_vocales = 0
n_consonantes = 0
n_espacios = 0
n_comas = 0
n_puntos = 0
c_letras = []
n_mayusculas = 0

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    if letra in consonantes:
        n_consonantes += 1
    if letra in espacios:
        n_espacios += 1
    if letra in comas:
        n_comas += 1
    if letra in puntos:
        n_puntos += 1
    if letra in vocales:
        c_letras.append(letra)
    if letra in mayusculas:
        n_mayusculas += 1


print("vocales: {}".format(n_vocales))
print("consonantes: {}".format(n_consonantes))
print("comas: {}".format(n_comas))
print("puntos: {}".format(n_puntos))
print("espacios: {}".format(n_espacios))
print(c_letras)
print("mayusculas: {}".format(n_mayusculas))

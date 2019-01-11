n_usuario = []
n_del_usuario = ""

while len(n_usuario) < 10:
    while not n_del_usuario.isdigit():
        n_del_usuario = input("Dime un numero: ")
    n_usuario.append(int(n_del_usuario))
    n_del_usuario = ""
    print("numero añadido")

print("la lista es {}".format(n_usuario))

n_grande = n_usuario[0]

for numero in n_usuario:
    if numero > n_grande:
        n_grande = numero

print("El numero mas grande es {}".format(n_grande))

n_peque = n_usuario[0]

for numero in n_usuario:
    if numero < n_peque:
        n_peque = numero

print("El numero mas pequeño es {}".format(n_peque))

cantidad_numeros = 0

for numero in n_usuario:
    cantidad_numeros += 1

print("La cantidad de numeros es {}".format(cantidad_numeros))

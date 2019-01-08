mi_lista = []

imput_usuario = input("¿Que quieres comprar? (Escribe fin si quieres terminar): ")

while imput_usuario != "fin":
    mi_lista.append(imput_usuario)
    imput_usuario = input("¿Que quieres comprar? (Escribe fin si quieres terminar): ")


largo_lista = len(mi_lista)
indice_actual = 0

# una forma de hacer una lista
while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("------------------------------------------")

# otra forma de hacer una lista
for item in mi_lista:
    print("tengo que comprar {}".format(item))

print("Esto tengo que comprar")

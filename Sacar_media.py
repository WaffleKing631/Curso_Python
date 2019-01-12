n_usuario = []
n_del_usuario = ""

while len(n_usuario) < 6:
    while not n_del_usuario.isdigit():
        n_del_usuario = input("Dime un numero: ")
    n_usuario.append(int(n_del_usuario))
    n_del_usuario = ""
    print("numero añadido")

suma = 0

for number in n_usuario:
    suma = suma + number

media = suma / len(n_usuario)
print("la media es {}".format(media))

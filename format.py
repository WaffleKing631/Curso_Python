# cambiar "A" o "a" en "VACA"
frase_usuario = input("Dime una frase: ")

frase_cam_A = frase_usuario.replace("A", "VACA")
frase_cam_a = frase_cam_A.replace("a", "VACA")

print(frase_cam_a)

print("----------------------------------------------------------------")
# se reemplaza todas las vocales por una i
frase_usuario_2 = input("Dime una frase: ")

frase_con_a = frase_usuario_2.replace("a", "i")
frase_con_e = frase_con_a.replace("e", "i")
frase_con_o = frase_con_e.replace("o", "i")
frase_con_u = frase_con_o.replace("u", "i")

print(frase_con_u)

print("----------------------------------------------------------------")
# se reemplazan las vocales por su numero de aparicion
# NO FUNCA, REPITO NO FUNCA

frase_usuario_3 = input("Dime un frase: ")
vocales = ["a", "e", "i", "o", "u"]
frase = None
number = 1

for letra in frase_usuario_3:
    if letra in vocales:
        frase = frase_usuario_3.replace(letra, str(number))
        number = number + 1

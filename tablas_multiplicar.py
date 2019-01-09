numero_tabla = int(input("¿Que numero quieres multiplicar?: "))


for multiplo in range(2, 11, 2):
    if multiplo * numero_tabla % 2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, multiplo * numero_tabla))

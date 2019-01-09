n_tabla = int(input("¿Que numero quieres multiplicar?: "))
n_multiplicar = 10

print("{} x {} = {}".format(n_tabla, n_multiplicar, n_tabla * n_multiplicar))
while n_multiplicar > 1:
    n_multiplicar -= 1
    print("{} x {} = {}".format(n_tabla, n_multiplicar, n_tabla * n_multiplicar))

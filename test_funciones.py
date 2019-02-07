# comprobar si un numero esta dentro de un rango de numeros


def numero_en_rango(numero_comprobar, minimo, maximo):
    comprobar_minimo = numero_comprobar >= minimo
    comprobar_maximo = numero_comprobar <= maximo
    if comprobar_maximo == comprobar_minimo is True:
        return True
    else:
        return False


print(numero_en_rango(10, 1, 100))
print(numero_en_rango(-5, -10, 5))
print(numero_en_rango(150, 1, 100))
print(numero_en_rango(10000, -500, 10005000))

print("---------------------------------------------------------------")
# devolver los pares de una lista de numeros


def devolver_pares(lista):
    lista_pares = []
    for item in lista:
        if item % 2 == 0:
            lista_pares.append(item)
    return lista_pares


print(devolver_pares([1, 2, 3, 4, 5, 6]))
print(devolver_pares([1, 2, 3, 4, 5, 6, 8, 51, 8415, 4810, 7946]))

print("---------------------------------------------------------------")
# encontrar numero mas grande entre 3 numeros


def numero_mas_grande(primero, segundo, tercero):
    if (primero > segundo) == (primero > tercero) is True:
        return primero
    if (segundo > primero) == (segundo > primero) is True:
        return segundo
    if (tercero > segundo) == (tercero > primero) is True:
        return tercero


print(numero_mas_grande(8, 156, 489))
print(numero_mas_grande(52, 5, 12))
print(numero_mas_grande(49, 489, 156))
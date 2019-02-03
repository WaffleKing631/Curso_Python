# ver cada clase de los datos en una lista

lista_datos = [1, 2, 3.1, "dsad", False, True, "sad", 3.2]
lista_tipos = []

for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)

print("-------------------------------------------------------------------------------------------")

# ver la cantidad de letras en cada string

lista_str = ["hola", "que pasa", "konichiwa", "arigato"]
lista_cant_str = []

for cant in lista_str:
    lista_cant_str.append(len(cant))

print(lista_cant_str)

print("-------------------------------------------------------------------------------------------")

# multiplicar los numeros de una lista

lista_number = [2, 3, 9, 9, 1, 8, 9]
lista_multi = None
suma = 1

for number in lista_number:
    suma = suma * number

print("la multiplicacion es {}".format(suma))

print("-------------------------------------------------------------------------------------------")

# sacar lista con cada clase de los datos

lista_mix = ["as", 2, "afha", 3, 8, 8, 9, "asd", "aksa", "das"]
lista_sel_str = []
lista_sel_int = []

for clas in lista_mix:
    if type(clas) == int:
        lista_sel_int.append(clas)
    else:
        lista_sel_str.append(clas)

print(lista_sel_int)
print(lista_sel_str)

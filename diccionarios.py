fechas = dict()
terminar = False


while not terminar:
    accion = input("¿Que quieres hacer? [añadir fecha de cumpleaños](a)/[consultar fecha de cumpleaños](c)/[salir](s) ")

    if accion == "a":
        print("vamos a añadir un numero: ")
        nombre = input("nombre: ")
        fecha = input("fecha de cumpleaños: ")
        fechas[nombre] = fecha

    elif accion == "c":
        print("consultar fecha de cumpleaños")
        nombre = input("de quien quieres saber la fecha de cumpleaños: ")
        print(fechas[nombre])

    elif accion == "s":
        terminar = True

print("---------------------------------------------------------------")
nombres_colores = {"rojo": "red", "amarillo": "yellow", "azul": "blue", "negro": "black", "blanco": "white",
                   "verde": "green", "cafe": "brown"}
salir = False

while not salir:
    accion = input("¿Que quieres hacer? [consultar color](c)/[salir](s)")
    if accion == "c":
        nombre_c = input("¿que color quieres saber?")
        print(nombres_colores[nombre_c])

    elif accion == "s":
        salir = True

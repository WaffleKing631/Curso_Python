import datetime

ahora = datetime.datetime.now()
ano = int(input("Dime el año: "))
mes = int(input("dime el mes: "))
dia = int(input("dime el día: "))
cumpleanos = datetime.datetime(year=ano, month=mes, day=dia)

faltante_cumple = cumpleanos - ahora

print("faltan {} días y {} horas para tu cumpleaños".format(faltante_cumple.days, int(faltante_cumple.seconds / 3600)))

if cumpleanos.weekday() == 0:
    print("y cae dia lunes")
elif cumpleanos.weekday() == 1:
    print("y cae dia martes")
elif cumpleanos.weekday() == 2:
    print("y cae dia miercoles")
elif cumpleanos.weekday() == 3:
    print("y cae dia jueves")
elif cumpleanos.weekday() == 4:
    print("y cae dia viernes")
elif cumpleanos.weekday() == 5:
    print("y cae dia sabado")
elif cumpleanos.weekday() == 6:
    print("y cae dia domingo")

print("----------------------------------------------------")

hoydia = datetime.datetime.now()
ano_2 = int(input("Dime el año: "))
mes_2 = int(input("dime el mes: "))
dia_2 = int(input("dime el día: "))
fecha = datetime.datetime(year=ano_2, month=mes_2, day=dia_2)

horas_pasadas = hoydia - fecha

print("han pasado {} horas".format(int(horas_pasadas.seconds / 3600 + horas_pasadas.days * 24)))

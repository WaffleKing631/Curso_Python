
import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 6
DRINKER_PENALIZATION = 3
SEDENTARY_PENALIZATION = 4


def barrabaja(message):
    print(message)
    print(len(message) * "-")


def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N" and response != "A veces":
        response = input(message + "[S/N/A veces]")
    return response


barrabaja("!Averigua cuanto te queda de vida¡")
print("Completa esta encuesta para saber cuanto tiempo de vida te queda")

birth_date = input("¿Cual es la fecha de tu cumpleaños? (formato: dd/mm/yyyy)")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
year_lost = 0

smoke = ask_yes_or_not("¿Fumas?")
if smoke == "S":
    year_lost += SMOKER_PENALIZATION
elif smoke == "A veces":
    year_lost += SMOKER_PENALIZATION / 2

drink = ask_yes_or_not("¿Bebes?")
if drink == "S":
    year_lost += DRINKER_PENALIZATION
elif drink == "A veces":
    year_lost += DRINKER_PENALIZATION / 2

sedentary = ask_yes_or_not("¿Haces deporte?")
if sedentary == "N":
    year_lost += SEDENTARY_PENALIZATION
elif sedentary == "A veces":
    year_lost += SEDENTARY_PENALIZATION / 2

base_lifespan = random.randint(AVERAGE_LIFESPAN / 2, AVERAGE_LIFESPAN)

lifespan = base_lifespan - year_lost
death_day = birth_date + datetime.timedelta(days=lifespan * 365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de tu muerte {}, te quedan {} dias para morir ".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))

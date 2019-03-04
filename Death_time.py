
import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 5
DRINKER_PENALIZATION = 3
SEDENTARY_PENALIZATION = 4


def barrabaja(message):
    print(message)
    print(len(message) * "-")


def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + "[S/N]")
    return response == "S"


barrabaja("!Averigua cuanto te queda de vida¡")
print("Completa esta encuesta para saber cuanto tiempo de vida te queda")

birth_date = input("¿Cual es la fecha de tu cumpleaños? (formato: dd/mm/yyyy)")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
year_lost = 0

if ask_yes_or_not("¿Fumas?"):
    year_lost += SMOKER_PENALIZATION

if ask_yes_or_not("¿Bebes?"):
    year_lost += DRINKER_PENALIZATION

if not ask_yes_or_not("¿Haces deporte?"):
    year_lost += SEDENTARY_PENALIZATION

base_lifespan = random.randint(AVERAGE_LIFESPAN / 2, AVERAGE_LIFESPAN)

lifespan = base_lifespan - year_lost
death_day = birth_date + datetime.timedelta(days=lifespan * 365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de tu muerte {}, te quedan {} dias para morir ".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))

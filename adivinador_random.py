import time
import random

print("¡Vamos a adivinar un numero!")

time.sleep(1)

number_to_guess = random.randint(1, 10)
user_number = int(input("Dime un numero: "))

print("Comprobando si adivinaste...")

if user_number == number_to_guess:
    time.sleep(3)
    print("Has adivinado el numero")
else:
    time.sleep(3)
    print("No has adivinado el numero, el numero era {}".format(number_to_guess))

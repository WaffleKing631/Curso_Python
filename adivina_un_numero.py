number_to_guess = 5

a = int(input("dime un numero?"))
b = int(input("dame otro numero?"))
c = int(input("solo uno mas"))

if a == number_to_guess:
    print("acertaste")
if b == number_to_guess:
    print("acertaste")
if c == number_to_guess:
    print("acertaste")
else:
    print("no has acertado :(")

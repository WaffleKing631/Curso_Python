print("Bienvenido a un combate pokemon, en este combate vas a "
      "contraolar a un pikachu que tiene 100 de vida, pelearas contra un charmander, un bulbasour o un squirtle")

pokemon_elejido = input("contra que pokemon quieres pelear (Squirtle / Bulbasour / Charmander): ")
# variables iniciales
hp_enemigo = 0
hp_pikachu = 100
nombre = 0
ataque = 0

# stats de los pokemons
if pokemon_elejido == "Squirtle":
    hp_enemigo = 90
    nombre = "Squirtle"
    ataque = 9
    print("Vas a pelear contra Squirtle que tiene 90 de vida")

elif pokemon_elejido == "Bulbasour":
    hp_enemigo = 120
    nombre = "Bulbasour"
    ataque = 8
    print("Vas a pelear contra Bulbasour que tiene 120 de vida")

elif pokemon_elejido == "Charmander":
    hp_enemigo = 80
    nombre = "Charmander"
    ataque = 12
    print("Vas a pelear contra Charmander que tiene 80 de vida")

# empieza el ciclo del combate
while hp_pikachu > 0 and hp_enemigo > 0:
    ataque_elegido = input("¿Que ataque quieres ocupar? (Bola voltio / Impactrueno): ")

    # se elije un ataque
    if ataque_elegido == "Bola voltio":
        hp_enemigo -= 10
    elif ataque_elegido == "Impactrueno":
        hp_enemigo -= 12

    print("Has ocupado {}".format(ataque_elegido))

    print("La vida del {} es {} hp".format(nombre, hp_enemigo))

    print("{} te hace {} de daño".format(nombre, ataque))
    hp_pikachu -= ataque

    print("La vida de pikachu es de {}".format(hp_pikachu))

if hp_enemigo <= 0:
    print("Has ganado, Felicidades")

if hp_pikachu <= 0:
    print("Has perdido, suerte para la proxima")

print("El combate ha terminado")
import random
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Entrenador: {self.nombre}"
class Pokemon:
    def __init__(self, nombre, ataque_maximo, vida_maxima):
        self.nombre = nombre
        self.ataque_maximo = ataque_maximo
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima
        self.ganadas = 0
        self.perdidas = 0

    def __str__(self):
        return f"{self.nombre} (Ataque: {self.ataque_maximo}, Vida: {self.vida_actual}/{self.vida_maxima})"

    def usarDadoDeAtaque(self):
        dado = random.randint(1, 6)
        if dado == 6:
            print("Ataque activado")
            return self.ataque_maximo
        else:
            return random.randint(0, self.ataque_maximo)

    def recuperar(self):
        self.vida_actual = self.vida_maxima

def crearEntrenadorPokemon():
    nombre_entrenador = input("Nombre del entrenador: ")
    nombre_pokemon = input("Nombre del Pokémon: ")
    ataque_maximo = random.randint(20, 100)
    vida_maxima = random.randint(150, 400)
    entrenador = Entrenador(nombre_entrenador)
    pokemon = Pokemon(nombre_pokemon, ataque_maximo, vida_maxima)
    return entrenador, pokemon

def calcularDanio(pokemon1, pokemon2):
    danio = pokemon1.usarDadoDeAtaque()
    pokemon2.vida_actual -= danio
    if pokemon2.vida_actual < 0:
        pokemon2.vida_actual = 0
    print(f"{pokemon1.nombre} hizo {danio} de daño a {pokemon2.nombre}. Vida restante: {pokemon2.vida_actual}")
    return danio

def simularPelea(pokemon1, pokemon2):
    print("\n--- PELEA COMENZANDO ---")
    calcularDanio(pokemon1, pokemon2)
    calcularDanio(pokemon2, pokemon1)

    if pokemon1.vida_actual > pokemon2.vida_actual:
        print(f"Ganador: {pokemon1.nombre}")
        pokemon1.ganadas += 1
        pokemon2.perdidas += 1
        return pokemon1
    elif pokemon2.vida_actual > pokemon1.vida_actual:
        print(f"Ganador: {pokemon2.nombre}")
        pokemon2.ganadas += 1
        pokemon1.perdidas += 1
        return pokemon2
    else:
        ganador = random.choice([pokemon1, pokemon2])
        print("Empate. Se elige ganador al azar.")
        print(f"Ganador: {ganador.nombre}")
        ganador.ganadas += 1
        if ganador == pokemon1:
            pokemon2.perdidas += 1
        else:
            pokemon1.perdidas += 1
        return ganador

def simulacion_Pokemos():
    print("Bienvenido a la simulacion del juego Pokémon")
    entrenador1, pokemon1 = crearEntrenadorPokemon()
    total_peleas = 0

    while True:
        opcion = input("\n¿Deseas pelear (P) o finalizar (F)? ").upper()
        if opcion == "F":
            break
        elif opcion == "P":
            entrenador2, pokemon2 = crearEntrenadorPokemon()
            pokemon1.recuperar()
            pokemon2.recuperar()
            ganador = simularPelea(pokemon1, pokemon2)
            total_peleas += 1
            print(f"\nGanador: {ganador.nombre} del entrenador {ganador.ganadas}")
            del entrenador2
            del pokemon2
        else:
            print("Opción inválida. Usa P o F.")

    print("\n--- RESUMENES DE LAS PELEAS ---")
    print(f"Total de peleas: {total_peleas}")
    print(f"{pokemon1.nombre} ganó {pokemon1.ganadas} y perdió {pokemon1.perdidas}")

simulacion_Pokemos()

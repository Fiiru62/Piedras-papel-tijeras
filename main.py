import random

# Bucle que continuará ejecutándose hasta que el jugador decida no jugar más
while True:  
    print("R: piedra, P: papel, S: tijeras")
    print()
    jugador = input("Selecciona que quieres jugar: ").lower()

    if jugador == "r" or jugador == "p" or jugador == "s":
        print("Seleccionaste " + jugador)

        # La máquina selecciona un número aleatorio entre 0 y 3
        maquina = random.randrange(0, 3)

        if maquina == 0:
            print("La máquina seleccionó piedra")
            print()
            if jugador == "r":
                print("Empate!")
            elif jugador == "p":
                print("Ganaste!")
            elif jugador == "s":
                print("Perdiste :c")
        elif maquina == 1:
            print("La máquina seleccionó papel")
            print()
            if jugador == "r":
                print("Perdiste :c")
            elif jugador == "p":
                print("Empate!")
            elif jugador == "s":
                print("Ganaste!")
        elif maquina == 2:
            print("La máquina seleccionó tijera")
            print()
            if jugador == "r":
                print("Ganaste!")
            elif jugador == "p":
                print("Perdiste :c")
            elif jugador == "s":
                print("Empate!")
    else:
        print("Debes seleccionar un valor posible para jugar")

    # espacio vacio en la consola
    print()
    
    # Preguntar si el jugador quiere seguir jugando
    seguir_jugando = input("¿Quieres seguir jugando? (si/no): ").lower()

    if seguir_jugando != "si":
        print("¡Gracias por jugar!")
        break  # Si la respuesta no es "si", el juego termina
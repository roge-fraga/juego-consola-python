from clases.jugador import Jugador
from clases.enemigo import Enemigo
import random


def main():
    nombre_jugador = input(
        "¡Bienvenido a la aventura en el Espacio! Por favor, ingresa tu nombre: "
    )
    jugador = Jugador(nombre_jugador)

    tipos_enemigos = [
        ("Alien", 50, 10),
        ("Robot", 30, 5),
        ("Monstruo", 70, 15),
    ]

    print("¡Comienza la aventura!")

    while True:
        enemigo_actual = Enemigo(*random.choice(tipos_enemigos))
        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino.")

        while enemigo_actual.salud > 0:
            accion = input("¿Que deseas hacer? (atacar/huir): ").lower()
            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} daño."
                )
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"El {enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de daño"
                    )
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate")
                break

        enemigo_derrotado = enemigo_actual.salud <= 0

        if jugador.salud <= 0:
            print("Has perdido la partida!")
            break

        if enemigo_derrotado:
            jugador.ganar_experiencia(20)

        continuar = input("¿Quieres seguir explorando? (s/n): ").lower()

        if continuar != "s":
            print("¡Gracias por haber jugado Batallas galacticas!")
            break


if __name__ == "__main__":
    main()

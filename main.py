import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador

# TODO: Añadir sistema de looteo, con mejoras para el jugador.
# TODO: Que cuando el jugador suba de nivel, los enemigos tambien sean mas dificiles.
# TODO: Permitir al usuario abandonar el juego siempre que quiera.
# TODO: Añadir chequeo de salida, preguntando si esta seguro de que desea salir.
# TODO: Establecer boss final para ganar el juego.
# TODO: Añadir detalle de salud restante del enemigo en combate y demas detalles.
# TODO: La barra de experiencia al vencer al enemigo deberia actualizarse antes del estado actual.
# TODO: Cuando la vida llega a 0 no deberia preguntarte si huis o atacas, deberia sacarte del programa.


def main():
    nombre_jugador = input(
        "¡Bienvenido a Batallas Galácticas! Por favor, ingresa tu nombre: "
    )
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15),
    ]

    enemigos_derrotados = []

    print("¡Comienza la aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)

        print("\n" + "=" * 45)
        print("🌌 NUEVO ENCUENTRO")
        print("=" * 45)
        print("🚀 Explorando el espacio...")
        print(f"👾 ¡Un {enemigo_actual.nombre} aparece frente a ti!")
        print("⚔️  ¡Prepárate para el combate!")

        while enemigo_actual.salud > 0:
            accion = input("¿Qué deseas hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"🎲 Tirada de ataque: {dano_jugador}")
                print(f"⚔️ Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño")
                enemigo_actual.recibir_dano(dano_jugador)
                print(f"👾 Salud del {enemigo_actual.nombre}: {enemigo_actual.salud}")

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"🎲 Tirada enemiga: {dano_enemigo}")
                    print(f"💥 El {enemigo_actual.nombre} te atacó y te causó {dano_enemigo} de daño")
                    jugador.recibir_dano(dano_enemigo)
                    
                jugador.mostrar_estado()

            elif accion == "huir":
                print("🏃‍♂️ Activando propulsores...")
                print("🚀 Has escapado del combate.")
                break

        if jugador.salud <= 0:
            print("\n" + "💀" * 35)
            print("💀 TU AVENTURA HA TERMINADO 💀")
            print("🌌 El universo ha reclamado tu destino...")
            print("💀" * 35)
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)
            jugador.ganar_experiencia(20)

        print("\n" + "-" * 45)  
        continuar = input("¿Quieres seguir explorando (s/n): ").lower()

        if continuar != "s":
            print("¡Gracias por haber jugado Batallas Galácticas!")
            break

    if not enemigos:
        print("\n" + "🏆" * 35)
        print("🏆 ¡HAS SALVADO LA GALAXIA! 🏆")
        print(f"🚀 {jugador.nombre} se convierte en una leyenda espacial.")
        print("🏆" * 35)


if __name__ == "__main__":
    main()

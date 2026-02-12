import random
import time


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud_maxima = 100
        self.salud = self.salud_maxima
        self.nivel = 1
        self.prob_critico = 0.2
        self.nivel_maximo = 3
        self.experiencia = 0

    def atacar(self):
        dano_base = random.randint(5, 15)

        critico = random.random() < self.prob_critico

        if critico:
            dano_base *= 2
            print("💥 ¡GOLPE CRÍTICO!")

        return dano_base

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0
            print(f"{self.nombre} ha muerto. ¡Game Over!")
        else:
            print(f"Te quedan {self.salud} puntos de salud.")

    def experiencia_necesaria(self):
        return 100 + (self.nivel - 1) * 20

    def mostrar_estado(self):
        print("\n📊 Estado actual:")
        print(f"❤️ {self.barra_vida()} {self.salud}/{self.salud_maxima}")
        print(f"⭐ Nivel: {self.nivel}")
        print(f"✨ {self.barra_xp()} {self.experiencia}/{self.experiencia_necesaria()}")
        print("-" * 30)

    def barra_vida(self, largo=20):
        porcentaje = self.salud / self.salud_maxima
        llenos = int(porcentaje * largo)
        vacios = largo - llenos
        return "█" * llenos + "-" * vacios

    def ganar_experiencia(self, experiencia):
        if self.nivel >= self.nivel_maximo:
            print("Has alcanzado el nivel máximo.")
            return  # Retorna None, es redundante agregarle None.

        self.experiencia += experiencia
        print(f"{self.nombre} ha ganado {experiencia} puntos de experiencia.")

        while (
            self.experiencia >= self.experiencia_necesaria()
            and self.nivel < self.nivel_maximo
        ):
            self.experiencia -= self.experiencia_necesaria()
            self.nivel += 1

            self.salud_maxima += 20
            self.salud = self.salud_maxima

            time.sleep(0.5)
            print("\n" + "✨" * 35)
            time.sleep(0.5)

            print("🚀✨ ¡¡¡ LEVEL UP !!! ✨🚀")
            time.sleep(0.5)

            print(f"🎉 {self.nombre} ahora es NIVEL {self.nivel}")
            time.sleep(0.5)

            print(f"💪 Salud máxima aumentada a {self.salud_maxima}")
            time.sleep(0.5)

            print("❤️ Salud restaurada completamente")
            time.sleep(0.5)

            print("✨" * 35 + "\n")

        if self.nivel == self.nivel_maximo:
            self.experiencia = 0
            print("Has alcanzado el nivel máximo.")

    def barra_xp(self, largo=20):
        necesaria = self.experiencia_necesaria()
        porcentaje = self.experiencia / necesaria
        llenos = int(porcentaje * largo)
        vacios = largo - llenos
        return "█" * llenos + "-" * vacios

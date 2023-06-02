# class 27: Proyecto: videojuego
import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elije un número del 1 al 100: "))
    contador = 1
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande...")
        else:
            print("Busca un número más pequeño...")
        numero_elegido = int(input("Elije otro número: "))
        contador += 1
    print()
    print("Ganaste!")
    print("Total de intentos: ", contador)


if __name__ == "__main__":
    run()

# class 26: Proyecto: prueba de primalidad


def es_primo(numero):
    if numero == 1:
        return False
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            return False
    return True


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print(str(numero) + " SI es primo")
    else:
        print(str(numero) +  " NO es primo")


if __name__ == "__main__":
    run()

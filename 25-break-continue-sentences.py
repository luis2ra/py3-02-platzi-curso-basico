# class 25: Interrumpiendo ciclos con break y continue


# Ejemplo 1
def run():
    for i in range(10000):
        print(i)
        if i == 5678:
            break


# # Ejemplo 2
# def run():
#     for contador in range(1000):
#         if contador % 2 != 0:
#             continue
#         print(contador)


# # Ejemplo 3
# def run():
#     texto= input('Escribe un texto: ')
#     for letra in texto:
#         if letra == 'o':
#             break
#         print(letra)


if __name__ == '__main__':
    run()

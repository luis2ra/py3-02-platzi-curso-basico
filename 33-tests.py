# test of codility


'''
Exercise: Dado un entero, imprimir por pantalla una secuencia de alteriscos *
'''
n = int(input("Ingresa la cantidad de * que desea imprimir: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" "),
#     print("")


'''
Exercise: Dado un entero, imprimir un triangulo invertido
'''
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end=" ")
    for j in range(2 * i - 1):
        print('*', end=" ")
    print("")


'''
Exercise: Dado un entero, contar cuantos digitos tiene usando bucles
'''
result = 0
while n > 0:
    n = n // 10
    result += 1
print("la cantidad de digitos es: ", result)

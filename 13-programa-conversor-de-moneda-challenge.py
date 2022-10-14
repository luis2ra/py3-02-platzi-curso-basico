# class 13: Tu primer programa: conversor de monedas

def exchanges(moneda, cantidad):
    result = 0
    # Moneda chilena
    if moneda == 1:
        result = cantidad * 0.0010
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dólares')
    # Moneda colombiana
    elif moneda == 2:
        result = cantidad * 0.00022
        print(f'Los {cantidad} pesos colombianos equivalen a {result} dólares')
    # Moneda argentina
    elif moneda == 3:
        result = cantidad * 0.0066
        print(f'Los {cantidad} pesos argentinos equivalen a {result} dólares')
    # Moneda mexicana
    elif moneda == 4:
        result = cantidad * 0.050
        print(f'Los {cantidad} pesos mexicanos equivalen a {result} dólares')
    # Otro
    else:
        print('Ingresa solo un numero de la lista')


if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres converti a dólares:
            [1] Moneda chilena a Dólar
            [2] Moneda colombiana a Dólar
            [3] Moneda argentida a Dólar
            [4] Moneda mexicana a Dólar
        Selecciona: '''))
        print('********************************')
        cantidad = int(input('Ingresa la cantidad que quieres convertir: '))
        exchanges(moneda, cantidad)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')

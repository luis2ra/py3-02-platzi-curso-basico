# class 13: Tu primer programa: conversor de monedas

# input del usuario
pesoscol = input("¿Cuantos pesos colombianos tienes?: ")
pesoscol = float(pesoscol)

# declaracion de valores (para hoy 14-10-2022)
valor_dolar = 4698.01
valor_euro = 4566.94
valor_cake = 20084.98
valor_btc = 89894072.34

# calculo valor dolar
dolares= pesoscol / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

# calculo Valor Euro
euros= pesoscol / valor_euro
euros = round(euros, 2)
euros = str(euros)

# calculo Cantidad de CAKE
cakes = pesoscol / valor_cake
cakes = round(cakes, 6)
cakes = str(cakes)

# calculo Bitcoin
btcs = pesoscol / valor_btc
btcs = round(btcs, 9)
btcs = str(btcs)

# prints
print("Tienes $ " + dolares + " dolares")
print("Tienes € " + euros + " Euros")
print("Tienes: " + cakes + " CAKE")
print("Tienes: " + btcs + " Bitcoins")

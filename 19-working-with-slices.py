# class 19: Trabajando con texto: slices


nombre = "Francisco"
print(nombre)
# "Francisco"


print(nombre[0:3])  # Arranca desde el primer índice hasta llegar antes del 3° índice.
# "Fra"


print(nombre[:3])  # Va desde el principio hasta antes de llegar del 3° índice. Cómo no hay ningún parámetro en el primer lugar, se interpreta que arranca desde el principio.
# "Fra"


print(nombre[1:7])  # Arranca desde el índice 1 hasta llegar antes del 7.
# "rancis"


print(nombre[1:7:2])  # Arranca desde el índice 1 hasta llegar antes del 7, pero pasos de 2 en 2, ya que eso es lo que nos indica el 3er parámetro, el cual es 2.
# "rni"


print(nombre[1::3])  # Arranca desde el índice 1 hasta el final del string (al no haber ningún 2do parámetro, significa que va hasta el final), pero en pasos de 3 en 3.
# "rcc"


print(nombre[::-1])  # Al no haber parámetro en los 2 primeros lugares, se interpreta que se arranca desde el inicio hasta el final, pero en pasos de 1 en 1 con la palabra al revés, porque es -1.
# "ocsicnarF"

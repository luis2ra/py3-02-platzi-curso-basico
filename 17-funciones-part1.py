# class 17: funciones

'''
definición de una función (con mas de un parametro)

En este caso, se usa la sentencia "return" para devolver
un valor en la setencia que invoca la función
'''
def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado  

sumatoria = suma(1, 4)  # se guarda el resultado en una variable
print(sumatoria)

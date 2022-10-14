# class 10: Los primitivos: tipos de datos sencillos
'''
Un objeto es una forma de modelar el mundo en programación. En los lenguajes 
de programación se caracterizan por tener métodos y atributos. En Python todo 
es un objeto.

Podemos encontrar cuatro tipos de datos que vienen definidos por defecto en 
Python, a estos tipos de datos los conocemos como primitivos.

Tipos de datos primitivos en Python:

- Integers: números Enteros
- Floats: números de punto flotante (decimales)
- Strings: cadena de caracteres (texto)
- Boolean: boolenaos (Verdadero o Falso)

Algunos operadores aritméticos pueden funcionar para operar con otros tipos de
datos. Por ejemplo: podemos sumar strings, lo que concatena el texto o 
multiplicar un entero por un string, lo que repetirá el "string" las veces 
que indique el entero.

Tipos de dato adicionales:
- Datos en texto: str
- Datos numéricos: int, float, complex
- Datos en secuencia: list, tuple, range
- Datos de mapeo: dict
- Set Types: set, frozenset
- Datos booleanos: bool
- Datos binarios: bytes, bytearray, memoryview

¿Cómo saber el tipo de dato que estoy usando?
Usamos el comando type()

'''

x = 5
print(type(x))

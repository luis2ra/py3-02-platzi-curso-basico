# class 31: Proyecto: generador de contraseñas
import random
import string


def generar_contrasena():
    caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    contrasena = []

    while (len(contrasena) < 16):
        caracteres=random.choice(caracter)    
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)  # genera un string a partir de una lista de caracteres
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == "__main__":
    run()

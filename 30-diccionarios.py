# class 30: ¿Qué son los diccionarios?


def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    
    for llave in mi_diccionario.keys():
        print(llave)
    
    for valores in mi_diccionario.values():
        print(valores)

    poblacion_paises = {
        'Argentina': 45810000,
        'Brasil': 214000000,
        'Colombia': 51270000
    }

    # print(poblacion_paises['Bolivia'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()

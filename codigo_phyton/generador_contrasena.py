import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J']
    minusculas = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']
    simbolos = ['¿', '{', '}', '.', '-', '_', '¡', '%', '!']
    numero = ['1', '2','3','4','5', '6', '7','8', '9','0']

    caracteres = mayusculas + minusculas + simbolos + numero

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)



if __name__ == '__main__':
    run()
import random

def run():
    numero_aleatorio = random.randint(1 , 100)
    numero_elegido = int(input ('Elige un número del 1 al 100: '))
    vidas = 10
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
            vidas -= 1
        elif numero_elegido > numero_aleatorio:
            print ('Busca un número más pequeño')
            vidas -= 1
        if vidas == 0:
            print('GAME OVER')
            break
        print('Tienes ', vidas , 'vidas')
        numero_elegido = int(input('Elige otro número: '))
    else:
        print('¡¡Ganaste!!')

if __name__ == '__main__':
    run()
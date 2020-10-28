#Para realizar una lista aleatoria
import random

#Definimos el algoritmo de ordenamiento
def ordenamiento_burbuja(lista):
    print('')
    n= len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            #indices de número a comparar
            if lista[j]> lista[j+1]:
                lista [j], lista[j+1]= lista[j+1], lista[j]
    return lista


if __name__=='__main__':
    tamano_de_lista =int(input('¿De qué tamaño es la lista? '))
    lista=[random.randint(0,100) for i in range(tamano_de_lista)]
    print('...............................................')
    print('Lista desordenada: ')
    print(lista)
    lista_ordenada=ordenamiento_burbuja(lista)
    print('Lista ordenada:')
    print(lista_ordenada)
    print('...............................................')
    
    
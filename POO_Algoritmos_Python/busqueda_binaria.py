#Para realizar una lista aleatoria
import random

#Definimos el algoritmo de busqueda
def busqueda_binaria(lista,comienzo, final, objetivo, intento):
    print('')
    #Contador de intentos
    print(f'Intento: {intento}')
    print(f'buscando {objetivo} entre: {lista[comienzo]} y {lista[final-1]}')
    print('')
    
    #Caso 1, objetivo, no esta en la lista
    if comienzo > final:
        return False
   
    medio= (comienzo+final)//2
    #Caso 2, la mitad de la lista es igual al objetivo
    if lista[medio]==objetivo:
        return True
    #Caso 3, el objetivo es mayor a la mitad de la lista   
    elif lista[medio]<objetivo:
        return busqueda_binaria(lista, medio +1, final, objetivo, intento+1)
    #Caso 4, el objetivo es menor a la mitad de la lista
    else:
        return busqueda_binaria(lista, comienzo, medio -1,objetivo, intento+1)

if __name__=='__main__':
    tamano_de_lista =int(input('¿De qué tamaño es la lista? '))
    objetivo=int(input('¿Qué número quieres encontrar? '))
    lista=sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    encontrado=busqueda_binaria(lista,0, len(lista), objetivo, intento=1)

    print(lista)
    print('')
    print(f'El elemento {objetivo} {", está" if encontrado else ", no está"} en la lista')
    print('...............................................')
    
    
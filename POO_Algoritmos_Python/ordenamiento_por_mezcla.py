#Para realizar una lista aleatoria
import random

#Definimos el algoritmo de ordenamiento por mezcla
def ordenamiento_por_mezcla(lista):
    if len(lista)>1:
        medio=len(lista)//2
        izquierda= lista[:medio]
        derecha=lista[medio:]

        #Verificar procesos
        print(izquierda, '-'*5, derecha)


        #Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iteradores para recorrer las dos sublistas
        i=0
        j=0

        #Iteradores para la lista principal
        k=0

        while i< len(izquierda) and j < len(derecha):
            if izquierda[i]<derecha[j]:
                lista[k]= izquierda[i]
                i += 1
            else:
                lista[k]=derecha[j]
                j +=1
            k+=1

        while i< len(izquierda):
            lista[k]=izquierda[i]
            i+= 1
            k+= 1

        while j< len(derecha):
            lista[k]=derecha[j]
            j+= 1
            k+= 1   
        
        print(f'Izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('.'*20)

    return lista  

if __name__=='__main__':
    tamano_de_lista =int(input('¿De qué tamaño es la lista? '))
    lista=[random.randint(0,100) for i in range(tamano_de_lista)]
    print('...............................................')
    print('Lista desordenada: ')
    print(lista)
    lista_ordenada=ordenamiento_por_mezcla(lista)
    print('Lista ordenada:')
    print(lista_ordenada)
    print('...............................................')
    
    
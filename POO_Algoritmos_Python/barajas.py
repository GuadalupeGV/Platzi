import random
import collections

PALOS= ['espada', ' corazon', 'rombo', 'trebol' ]
VALORES= ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']


#1.- Función que ayuda a generar baraja (combinaciones)
def crear_baraja():
    barajas=[]
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    return barajas

#3.- Función para obtener mano
def obtener_mano(barajas, tamano_mano):
    #Permite obtener una muestra de la población
    mano= random.sample(barajas, tamano_mano)
    return mano

#2. Definir main
def main(tamano_mano, intentos):
    barajas=crear_baraja()

    #Guarda los intento de las manos en simulacion
    manos= []
    for _ in range (intentos):
        mano=obtener_mano(barajas, tamano_mano)
        #Añadimos mano creada a manos
        manos.append(mano)
    
#4. Calcular probabilidad de que salga pares en la mano obtenida
    pares = 0
    for mano in manos:
        valores= []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))

        for val in counter.values():
            if val ==2:
                pares += 1
                break
    perobabilidad_par= pares/ intentos
    print (' '*20) 
    print(f'La probabilidad de obtener un par en una mano del {tamano_mano} barajas es {perobabilidad_par} ')


#Calcular probabilidad de que salga una corrida




#Definir por el usuario, el tamaño de la mano y los intentos
if __name__=='__main__':
    tamano_mano= int(input('¿De cuántas barajas será la mano? '))
    intentos= int(input('¿Cuántos intentos para calcular la probabilidad? '  ))
    
    main(tamano_mano,intentos)
    print('_'* 60)
    
   
import random
import math
from estadisticas import desviacion_estandar, media

def aventar_agujas (numero_agujas):
    adentro_del_circulo= 0

    for _ in range(numero_agujas):
        x= random.random* random.choice([-1, 1])
        y= random.random* random.choice([-1, 1])
        
        distancia_centro= math.sqrt (x**2 + y**2)

        if distancia_centro <= 1:
            adentro_del_circulo += 1
        
    
    return (4* adentro_del_circulo)/numero_agujas

    #Estadistica inferencial
def estimacion(numero_agujas, numero_de_intentos):
    estimados= []
    for _ in range(numero_de_intentos):
        estimacion_pi= aventar_agujas(numero_agujas)
        estimados.append(estimacion_pi)
        
    media_estimado=media(estimados)
    sigma=desviacion_estandar(estimados)
    print(' '* 20)
    print (f' Estimado= {round(media_estimado, 5)},Signma= {round(sigma,5)}, Agujas totales= {numero_agujas} ')
    
    return (media_estimado, sigma)

#Calculo de la presición de la simulación
def estimar_pi (presición, numero_de_intentos):
    numero_agujas=1000
    sigma =presición

    while sigma >= presición/1.96:
        media, sigma=estimacion(numero_agujas,numero_de_intentos)
        numero_agujas*= 2

    return media

#Generar 
 
if __name__ == ' __main__':
    estimar_pi(0.01, 1000)



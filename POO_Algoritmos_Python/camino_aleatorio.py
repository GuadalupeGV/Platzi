from borracho import BorrachoTradicional
from campo import Campo
from coordenada_abstraccion import Coordenada

#5
def caminata(campo, borracho,pasos):
    x_arreglo=[]
    y_arreglo=[]
    inicio=campo.obtener_coordenada(borracho)
    x_arreglo.append(donde_se_movio.x)
    y_arreglo.append(donde_se_movio.y)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        donde_se_movio=campo.obtener_coordenada(borracho)
        x_arreglo.append(donde_se_movio.x)
        y_arreglo.append(donde_se_movio.y)
    
    graficar(x_arreglo, y_arreglo)
    return inicio.distancia(campo.obtener_coordenada(borracho))

#4
def simular_caminata(pasos, numero_de_intentos, tipo_borracho):
    borracho= tipo_borracho(nombre='David')
    origen= Coordenada(0,0)
    distancias=[]

    for _ in range(numero_de_intentos):
        campo=Campo()
        campo.anadir_borracho(borracho,origen)
        simulacion_caminata=caminata(campo,borracho, pasos)
        distancias.append(round(simulacion_caminata))
    
    return distancias

def graficar (x,y):
    grafica =figure(title='Camino Aleatorio Borrachos', x_axis_lab='Pasos', y_axis_label='Distancia')
    grafica.line(x,y, legend='Distancia media')
    show(grafica)



#3
def main(distancias_de_caminata,numero_de_intentos,tipo_borracho):
    distancias_media_por_caminata=[]
    for pasos in distancias_de_caminata:
        distancias=simular_caminata(pasos,numero_de_intentos,tipo_borracho)
        print(len(distancias))
        #7
        distancia_media=round(sum(distancias) / len(distancias),4)
        distancia_maxima= max(distancias)
        distancia_minima= min(distancias)
        print (f'{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media= {distancia_media} ')
        print(f'Max= {distancia_maxima}')
        print(f'Min= {distancia_minima}')

#2
if __name__=='__main__':
    distancias_de_caminata=[10,100,1000,10000]
    numero_de_intentos=1

    main(distancias_de_caminata,numero_de_intentos,BorrachoTradicional)



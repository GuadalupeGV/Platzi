#importamos librería para evitar el error por límite de ejecución y determinarlo
import sys

#definición de función
def fibonacci_dinamico(n, memo={}):
    if n==0 or n==1:
        return 1
    #Guardar recursiones en diccionario
    try:
        return memo[n]
    except KeyError:
        resultado= fibonacci_dinamico(n-1, memo)+ fibonacci_dinamico(n-2, memo)
        memo[n]=resultado
        return resultado

#Iniciamos
if __name__=='__main__':
    sys.setrecursionlimit(10002)
    
    n=int(input('Ingrese un número: '))
    resultado=fibonacci_dinamico(n)

    print('.'*40)
    print(f'El número Fibonacci es=  ')
    print (resultado)
    print('.'*40)
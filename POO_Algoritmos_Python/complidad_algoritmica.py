import time

#Primer algoritmo
def factorial(n):
    respuesta=1

    while n>1:
        respuesta *=n
        n -=1
       
    return respuesta

#Segundo algoritmo
def factorial_r(n):
    if n==1:
        return 1
           
    return n*factorial(n-1)

if __name__=='__main__':
    n=200000

#time
comienzo=time.time()
factorial(n)
final=time.time()
print(' ')
print('Primer algorítmo')
print(final-comienzo)
print('....................')

comienzo=time.time()
factorial(n)
final=time.time()
print(' ')
print('Segundo algorítmo')
print(final-comienzo)
print('....................')



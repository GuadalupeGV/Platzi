dolares= float(input("¿Cuántos dólares tienes: "))
valor_peso= 0.048
pesos = dolares / valor_peso
pesos = round(pesos,2)
pesos =str(pesos)
print("Tienes $" + pesos + " pesos mexicanos")

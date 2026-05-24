def calcular_maximo(lista):
    
    maior = lista[0]
    
    for numero in lista:
        if numero > maior:
            maior = numero
            
    return maior



print(calcular_maximo([3, 20, 9000]))
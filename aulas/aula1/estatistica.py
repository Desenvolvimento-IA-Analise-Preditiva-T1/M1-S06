def calcular_maximo(lista):
    """Retorna o maior valor de uma lista sem usar max()."""
    
    maior = lista[0]  # Assume que o primeiro é o maior
    for numero in lista:
        if numero > maior:
            maior = numero  # Atualiza se encontrar um maior
    return maior


def calcular_minimo(lista):
    """Retorna o menor valor de uma lista sem usar min()."""
    
    menor = lista[0]  # Assume que o primeiro é o menor
    for numero in lista:
        if numero < menor:
            menor = numero  # Atualiza se encontrar um menor
    return menor


def calcular_media(lista):
    """Retorna a média dos valores de uma lista sem usar sum()."""

    soma = 0
    for numero in lista:
        # soma += numero  # Acumula o valor de cada elemento
        soma = soma + numero
    return soma / len(lista)


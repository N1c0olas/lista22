numeros = input("Digite uma lista de numeros separados por espaços: ").split()
numeros = [int(numero) for numero in numeros]

numeros.sort(reverse=True)

print("Lista ordenada em ordem decrescente:", numeros)

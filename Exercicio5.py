numeros = input("Digite uma lista de numeros separados por espaços: ").split()
numeros = [int(numero) for numero in numeros]
numeros.sort()

print("Lista ordenada em rdem crescente:", numeros)
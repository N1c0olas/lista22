numeros = input("Digite uma lista de numeros sparados por espaços: ").split()
numeros = [int(numero) for numero in numeros]
numeros.sort()

print("O numero minimo é:", numeros[0])
print("O numero maximo é:", numeros[-1])

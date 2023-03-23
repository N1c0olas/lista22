numeros = input("Digite uma lista de numeros separados por espaços: ").split()
numeros = [int(numero) for numero in numeros]
soma = sum(numeros)
media =  soma / len(numeros)

print("A media dos numeros é:", media)

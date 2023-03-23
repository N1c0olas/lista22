lista_numeros = input("Digite uma lista de números separados por vírgula: ")
lista_numeros = lista_numeros.split(",")

for numero in lista_numeros:
    if float(numero) > 10:
        print(numero)
numeros = input("Digite uma lista de números, separados por vírgula: ")
numeros = numeros.split(",")  

for num in numeros:
    if int(num) % 2 == 0: 
        print(num)

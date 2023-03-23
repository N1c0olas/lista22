palavras = input("Digite uma lista de palavras separadas por espaços: ").split()
palavras_a = []

for palavra in palavras:
    if palavra.startswith('a') or palavra.startswith('A'):
        palavras_a.append(palavra)
        
print("Palavras que começam com a letra 'a' :")
for palavra in palavras_a:
    print(palavra)
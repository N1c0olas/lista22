nomes = input("Digite uma lista d nomes separados por espaços: ").split()

nome_mais_longo = max(nomes, key=len)
nome_mais_curto = min(nomes, key=len)

print("O nome mais longo é:", nome_mais_longo)
print("O nome mais curto é:", nome_mais_curto)

#arqv = open("arquivo.txt", "w")
"""arqv = open("arquivo.txt")
linhas = arqv.readlines()
nomes = []
for linha in linhas:
    print(linha)
    nomes.append(linha)
print(nomes)"""
"""with open("arquivo.txt") as aqv:
    linhas = aqv.readlines()
    nomes = []
    for linha in linhas:
        print(linha)
        nomes.append(linha)
print(nomes)"""

with open("Teste.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    nomes = []
    for linha in linhas:
        print(linha)
        nomes.append(linha.strip())
print(nomes)

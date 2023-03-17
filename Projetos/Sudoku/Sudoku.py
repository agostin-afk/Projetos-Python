dimensao = int(input('informe a dimensao da tabela: '))


def montarTabela(dimensao):
    tabela = [[] for _ in range(dimensao)]
    for linha in range(dimensao):
        for coluna in range(dimensao):
            x = int(input(f'posicao {linha +1} x {coluna +1}: '))
            tabela[linha].append(x)
    return tabela


tabela = montarTabela(dimensao)
for linha in range(dimensao):
    for coluna in range(dimensao):
        print(f'{tabela[linha][coluna]:^4}', end=' ')
    print()


def bloco(t):
    linha = coluna = 0
    while linha < dimensao // 2:
        while coluna < dimensao // 2:
            print(t[linha][coluna], end=' ')
            coluna += 1
        print()
        linha += 1
        coluna = 0
bloco(tabela)

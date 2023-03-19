def montarTabela():
    dimensao = int(input('informe a dimensao da tabela: '))
    tabela = []
    for linha in range(dimensao):
        linha_atual = []
        for coluna in range(dimensao):
            x = int(input(f'posicao {linha +1} x {coluna +1}: '))
            linha_atual.append(x)
        tabela.append(linha_atual)
    return tabela


def exibir_blocos(tabela, tamanho=2):
    bloco = []
    items = []
    for linha in range(0, len(tabela), tamanho):
        for coluna in range(0, len(tabela[0]), tamanho):
            aux = []
            for i in range(tamanho):
                for j in range(tamanho):
                    if coluna + j < len(tabela[0]):
                        print(f'{tabela[linha+i][coluna+j]:^4}', end=' ')
                        x = tabela[linha+i][coluna+j]
                        aux.append(x)
                print()
            bloco.append(aux[:])
            print('-'*30)
    print(bloco)
t = montarTabela()
exibir_blocos(t)
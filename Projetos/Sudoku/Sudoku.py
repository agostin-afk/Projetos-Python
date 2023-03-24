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
    return bloco
def linhas_separadas(t):
    linhas = []
    for linha in range(0, len(t)):
        aux = []
        for coluna in range(0, len(t)):
            aux.append(t[linha][coluna])
        linhas.append(aux[:])
    print(linhas)
def colunas_separadas(t):
    colunas = []
    for coluna in range(0, len(t)):
        aux = []
        for linha in range(0, len(t)):
            aux.append(t[linha][coluna])
        colunas.append(aux[:])
    print(colunas)
def checagem_bloco(bloco):
    bloco_repeticao = []
    for x in range(0, 3):
        tem_repetidos = len(bloco[x]) != len(set(bloco[x]))
        if tem_repetidos:
            bloco_repeticao.append(x+1)
    return(bloco_repeticao)
t = montarTabela()
p = exibir_blocos(t)
print(checagem_bloco(p))
linhas_separadas(t)
colunas_separadas(t)
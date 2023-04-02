"""def montarTabela():
    dimensao = int(input('informe a dimensao da tabela: '))
    tabela = []
    for linha in range(dimensao):
        linha_atual = []
        for coluna in range(dimensao):
            x = int(input(f'posicao {linha +1} x {coluna +1}: '))
            linha_atual.append(x)
        tabela.append(linha_atual)
    return tabela


def blocos_separados(tabela, tamanho=2):
    bloco = []
    for linha in range(0, len(tabela), tamanho):
        for coluna in range(0, len(tabela[0]), tamanho):
            aux = []
            for i in range(tamanho):
                for j in range(tamanho):
                    if coluna + j < len(tabela[0]):
                        #print(f'{tabela[linha+i][coluna+j]:^4}', end=' ')
                        x = tabela[linha+i][coluna+j]
                        aux.append(x)
                #print()
            bloco.append(aux[:])
            #print('-'*30)
    #print(bloco)
    return bloco


def linhas_separadas(tabela):
    linhas = []
    '''for linha in range(0, len(tabela)):
        aux = []
        for coluna in range(0, len(tabela)):
            aux.append(tabela[linha][coluna])
        linhas.append(aux[:])'''
    linhas = tabela[:]
    return linhas


def colunas_separadas(tabela):
    colunas = []
    for coluna in range(0, len(tabela)):
        aux = []
        for linha in range(0, len(tabela)):
            aux.append(tabela[linha][coluna])
        colunas.append(aux[:])
    return colunas


def conferir(blocos, linhas, colunas):
    tabela_completa = [[],[]]
    while True:
        numeros = [1,2,3,4,5,6,7,8,9]
        for i in range(len(linhas)):
            for num in range(len(linhas)):
                for j in range(len(colunas)):
                    if numeros[num] not in linhas[i] and numeros not in colunas[j]:
                        tabela_completa[i].append(numeros[num])
        break
    return tabela_completa


tabela = montarTabela()
blocos = blocos_separados(tabela)
linhas = linhas_separadas(tabela)
colunas = colunas_separadas(tabela)
teste = conferir(blocos, linhas, colunas)
print(f'{tabela}\n{blocos}\n{linhas}\n{colunas}\n\n\n{teste}')
"""


def criar_tabela():
    global x
    try:
        x = int(input('qual a dimensão da tabela ?[4/9]: '))
        while True:
            if x in [4,9]:
                break
            else:
                x = int(input('por favor, escolha entre 4 e 9'))
    except (ValueError, NameError, TypeError):
        print('Erro de tipo, informe um valor inteiro')
    except KeyboardInterrupt:
        print('Sistema interrompido pelo usuario')
    tabela = [[] for _ in range(x)]
    return tabela
def preencher_tabela(tabela):
    tamanho =  len(tabela)
    for i in range(tamanho):
        for j in range(tamanho):
            num = int(input(f'Informe o valor da celula {i+1}x{j+1}: '))
            tabela[i].append(num)
    tabela_preenchida = tabela[:]
    return tabela_preenchida
teste = criar_tabela()
p = preencher_tabela(teste)
print(p)

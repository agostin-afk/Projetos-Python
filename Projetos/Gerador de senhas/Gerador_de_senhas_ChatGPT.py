import os.path
import random
import time


def gerar_senhas(compri_senha, incluir_numeros, num_senhas):
    senhas = []
    caracteres = 'qwertyuiopasdfghjklçzxcvbnm!@#$%&*_-=+QWERTYUIOPASDFGHJKLÇZXCVBNM'
    if incluir_numeros:
        caracteres += '0123456789'
    for i in range(num_senhas):
        password = ''
        for c in range(compri_senha):
            password += random.choice(caracteres)
        senhas.append(password)
    return senhas


def criar_arquivo(nome_arquivo):
    try:
        open(nome_arquivo, 'xt').close()
    except FileExistsError:
        print(f'O arquivo "{nome_arquivo}" já existe.')
    except:
        print('Erro na criação do arquivo.')


def gravar_senhas(nome_arquivo, senhas):
    dicionario_senhas = {}
    for senha in senhas:
        nome_usuario = input(f'Informe um nome de usuário para a senha "{senha}": ')
        dicionario_senhas[senha] = nome_usuario
    try:
        with open(nome_arquivo, 'at') as arquivo:
            for senha, nome_usuario in dicionario_senhas.items():
                arquivo.write(f'{nome_usuario} -> {senha}\n')
        print(f'As senhas foram salvas no arquivo "{nome_arquivo}" com sucesso.')
    except:
        print(f'Erro ao escrever no arquivo "{nome_arquivo}".')


def ler_senhas(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        criar_arquivo(nome_arquivo)
        return
    try:
        with open(nome_arquivo, 'rt') as arquivo:
            print('-'*30)
            while True:
                resposta = input('Deseja catalogar as suas senhas? [S/N]: ').upper()[0]
                if resposta in 'SN':
                    break
                else:
                    print('Por favor, responda Sim ou Não.')
            if resposta == 'S':
                senhas = [linha.strip().split(' -> ')[-1] for linha in arquivo]
                gravar_senhas(nome_arquivo, senhas)
            else:
                for indice, linha in enumerate(arquivo, start=1):
                    print(f'{indice}: {linha.strip()}')
    except Exception as erro:
        print(f'Erro ao ler o arquivo: {erro}')


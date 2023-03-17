import random
import time

'''
def senha(lenth=10, num=False, qtd_senhas=10):
    senhas = []
    carateres = 'qwertyuiopasdfghjklçzxcvbnm!@#$%&*_-=+QWERTYUIOPASDFGHJKLÇZXCVBNM0123456789'
    for i in range(0, qtd_senhas):
        password = ''
        if num:
            for c in range(0, lenth):
                password += random.choice(carateres)
        else:
            carateres = 'qwertyuiopasdfghjklçzxcvbnm!@#$%&*_-=+QWERTYUIOPASDFGHJKLÇZXCVBNM'
            num = True
            i -= 1
        i += 1
        if i != 0:
            senhas.append(password)
    for x, p in enumerate(senhas):
        print(f'{x + 1}º senha -> {p}')
        time.sleep(0.5)
    return senhas


def parametos():
    global compri_senha, num_senhas, n
    while True:
        try:
            while True:
                num = input('Deseja numeros nas suas senhas ?[S/N]: ').upper().split()[0]
                num = num[0]
                if num not in "SN":
                    print('Por favor, responda Sim ou Não. ')
                    continue
                else:
                    break
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
            break
        else:
            if num == 'S':
                n = True
            else:
                n = False
            break
    while True:
        try:
            compri_senha = int(input('Informe o numero de digitos da sua senha: '))
        except (ValueError, TypeError):
            print('Informe um valor numerico.')
            continue
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
        else:
            break
    while True:
        try:
            num_senhas = int(input('Informe o numero de senhas para serem geradas: '))
        except (ValueError, TypeError):
            print('Informe um valor numerico.')
            continue
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
        else:
            break
    x = senha(compri_senha, n, num_senhas)
    while True:
        try:
            while True:
                salvar = input('Deseja salvar as suas senhas ?[S/N]: ').upper().split()[0]
                salvar = salvar[0]
                if salvar not in "SN":
                    print('Por favor, responda Sim ou Não. ')
                    continue
                else:
                    break
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
        else:
            if salvar == 'S':
                nome_arquivo = input('informe o nome do arquivo: ')
                nome_arquivo += '.txt'
                ler(nome_arquivo)
                if ler(nome_arquivo):
                    Escrever(nome_arquivo, x)
                else:
                    print('Erro para escrever o arquivo')
            else:
                print('Programa finalizado')
            break
    return x

def ler(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        criar(nome)
    if criar(nome):
        return True
    else:
        return False


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
        return False
    else:
        print(f'Arquivo {nome} criado')
        return True


def Escrever(nome, x):
    global a
    try:
        a = open(nome, 'at')
    except:
        print('Erro para abrir o arquivo')
    else:
        for v in x:
            a.write(f'{v}\n')
        print('nomes gravados com sucesso')
    finally:
        a.close()

lista_senhas = parametos()
'''


def senha(lenth=10, num=False, qtd_senhas=10):
    senhas = []
    carateres = 'qwertyuiopasdfghjklçzxcvbnm!@#$%&*_-=+QWERTYUIOPASDFGHJKLÇZXCVBNM0123456789'
    for i in range(0, qtd_senhas):
        password = ''
        if num:
            for c in range(0, lenth):
                password += random.choice(carateres)
        else:
            carateres = 'qwertyuiopasdfghjklçzxcvbnm!@#$%&*_-=+QWERTYUIOPASDFGHJKLÇZXCVBNM'
            num = True
            i -= 1
        i += 1
        if i != 0:
            senhas.append(password)
    for x, p in enumerate(senhas):
        print(f'{x + 1}º senha -> {p}')
        time.sleep(0.5)
    return senhas


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado')


def ler(nome):
    global ask_login
    print('-'*30)
    while True:
        try:
            while True:
                ask_login = input('Deseja catalogar as suas senhas ?[S/N]: ').upper().split()[0]
                ask_login = ask_login[0]
                if ask_login not in "SN":
                    print('Por favor, responda Sim ou Não. ')
                else:
                    break
            break
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
            break
    while True:
        try:
            a = open(nome, 'rt')
            a.close()
        except FileNotFoundError:
            criar(nome)
            break
    Escrever(nome, senhas, True if ask_login == 'S' else False)


def Escrever(nome, x, login=False):
    global a, dicionario
    try:
        a = open(nome, 'at')
    except:
        print('Erro para abrir o arquivo')
    else:
        if not login:
            for v in x:
                a.write(f'{v}\n')
            print('nomes gravados com sucesso')
        if login:
            dicionario = {}
            num = 0
            for c in senhas:
                nome_senha = input(f'informe um nome de usuario para a senha: {senhas[num]}\n ')
                dicionario[c] = nome_senha
                num += 1
        for k, v in dicionario.items():
            a.write(f'{v} -> {k}\n')
        print('Nomes gravados com sucesso')
    finally:
        a.close()


def arquivo_login():
    while True:
        try:
            while True:
                print('-'*30)
                ask = input('Deseja salvar as suas senhas? [S/N]: ').upper().split()[0]
                ask = ask[0]
                if ask not in 'SN':
                    print('Por favor, responda sim ou não.')
                    continue
                else:
                    break
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuario')
            break
        else:
            try:
                if ask == 'S':
                    nome_arquivo = input('informe o nome do arquivo: ')
                    nome_arquivo += '.txt'
                    ler(nome_arquivo)
            except KeyboardInterrupt:
                print('\nSistema interrompido pelo usuario')
            break
    print('Programa finalizado com sucesso!!')


def parametos():
    global compri_senha, num_senhas, n
    while True:
        try:
            while True:
                num = input('Deseja numeros nas suas senhas ?[S/N]: ').upper().split()[0]
                num = num[0]
                if num not in "SN":
                    print('Por favor, responda Sim ou Não. ')
                    continue
                else:
                    break
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
            break
        else:
            if num == 'S':
                n = True
            else:
                n = False
            break
    while True:
        try:
            compri_senha = int(input('Informe o numero de digitos da sua senha: '))
        except (ValueError, TypeError):
            print('Informe um valor numerico.')
            continue
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
        else:
            break
    while True:
        try:
            num_senhas = int(input('Informe o numero de senhas para serem geradas: '))
        except (ValueError, TypeError):
            print('Informe um valor numerico.')
            continue
        except KeyboardInterrupt:
            print('Sistema interrompido pelo usuário.')
        else:
            break
    x = senha(compri_senha, n, num_senhas)
    return x


senhas = parametos()

arquivo_login()

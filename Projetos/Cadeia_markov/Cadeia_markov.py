import numpy as np


corpus =open(r'A:\\agostinho\\codigos\\Projetos-Python\\Projetos\\Cadeia_markov\\palavras.txt',encoding='utf8').read().split()


def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        

pares_palavras = make_pairs(corpus)


dict_palavras = {}
for palavra_1, palavra_2 in pares_palavras:
    if palavra_1 in dict_palavras.keys():
        dict_palavras[palavra_1].append(palavra_2)
    else:
        dict_palavras[palavra_1] = [palavra_2]
     
primeira_palavra = np.random.choice(corpus)
cadeia_palavras = [primeira_palavra]
numero_palavras = 7
        
for i in range(numero_palavras):
    if cadeia_palavras[-1] in dict_palavras: 
        cadeia_palavras.append(np.random.choice(dict_palavras[cadeia_palavras[-1]]))
    else:
        break
' '.join(cadeia_palavras)
print(' '.join(cadeia_palavras))
import random

pesos = [90, 10]

dict_teste = {
    'Agosto': 'Ferreira',
    'Ferreira': 'Dale papai',
              }
#for k,v in dict_teste.items():
#    print(f'{k} -> {v}')
    
dici_dict = {
    "agosto": {"ferreira": pesos[0]},
    "Ferreira": {"Dale papai": pesos[1]},
}
for k, i in dici_dict.items():
    print(f'{k} -> {list(i.keys())[0]} -> {int(list(i.values())[0])}')
print(dici_dict)
    
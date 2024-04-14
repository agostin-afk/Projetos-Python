import random
import os
lista_exemplo = ["essa", "é", "uma", "lista"]
lista_exemplo_numerico = [1,5,6,3,45]

lista_result = []

for i in range(100):
    
    lista_result.extend(random.choices(lista_exemplo_numerico))

os.system("cls")

print(lista_result.count(45))
print(lista_result.count(1))
print(lista_result.count(5))
print(lista_result.count(6))
print(lista_result.count(3))
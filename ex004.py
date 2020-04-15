#4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possiveis sobre ele.
"""
n1 = input('digite algo:' ) #boolean = True ou False
print(n1.isnumeric())

n2 = input('Digite algo: ') #verificando se é alfabetico 
print(n2.isalpha())

n3 = input('Digite algo: ') #verificar se alfanumerico 
print(n3.isalnum())

n4 = input('Digite algo: ') #verificar se alfanumerico 
print(n4.isalnum())

n5 = input('Digite algo: ') # verifica se está em letra maiscula
print(n5.isupper())
"""


a = input('Digite algo ')

print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaço? ', a.isspace()) 
print('É um número?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumérico', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúculas?', a.islower())
print('Está capitalizada?', a.istitle)










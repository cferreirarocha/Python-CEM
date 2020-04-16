#007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2

print(f'A média entre {n1:.1f} e {n2:.1f} é igual {m:.1f}')
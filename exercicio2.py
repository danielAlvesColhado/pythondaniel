# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

n1 = float(input('Digite um numero: '))

print(f'é um numero inteiro?')
if int(n1) == n1:
    print(f'{n1} é um numero inteiro!')
else:
    print(f'{n1} é um numero decimal!')
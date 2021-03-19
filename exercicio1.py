#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

n1 = int(input('Digite um numero inteiro: '))
e_par = n1 % 2 == 0
print(f'o numero {n1} é par? {e_par}')
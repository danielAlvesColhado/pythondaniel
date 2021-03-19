#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

n1 = float(input('Informe um numero: '));
n2 = float(input('Informe mais um numero: '));
decisao = input('qual operaçao deseja realizar? digite 1 - soma, 2 - subtraçao, 3 - divisao, 4 - multiplicaçao');

if decisao == '1':
    print(f'a soma dos numeros é {n1 + n2}')
    e_par = (n1 + n2) % 2 == 0
    print(f'a soma dos numeros é par? {e_par}')
elif decisao == '2':
    print(f'{n1} - {n2} = {n1 - n2}')
    if (n1 - n2) > 0:
        print('é um numero positivo!')
    elif (n1 - n2) < 0:
        print('é um numero negativo')
    else: print('é um numero neutro!')
elif decisao == '3':
    divisao = float(n1 / n2)
    print (f'{n1} dividido por {n2} = {divisao}')
    if int(divisao) == divisao:
        print(f'{divisao:.2f} é um numero inteiro!')
    else:
        print(f'{divisao:2f} é um numero decimal!')

elif decisao == '4':
    print(f'o resultado da multiplicaçao é {n1 * n2}')
    e_par = (n1 * n2) % 2 == 0
    print(f'a soma dos numeros é par? {e_par}')
else:
    print ('tente novamente')
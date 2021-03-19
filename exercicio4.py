#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".
contagem = 0
print('responda as perguntas a seguir Apenas com SIM ou NAO')
p1 = input('Telefonou para a vítima? ')
if p1 == 'SIM':
    contagem = contagem + 1
elif p1 != 'NAO':
    print('Recarregue o programa e digite SIM ou NAO apenas!'), quit()
p2 = input('Esteve no local do crime?')
if p2 == 'SIM':
    contagem = contagem + 1
elif p2 != 'NAO':
    print('Recarregue o programa e digite SIM ou NAO apenas!'), quit()
p3 = input('mora perto da vítima? ')
if p3 == 'SIM':
    contagem = contagem + 1
elif p3 != 'NAO':
    print('Recarregue o programa e digite SIM ou NAO apenas!'), quit()
p4 = input('Devia para a vítima? ')
if p4 == 'SIM':
    contagem = contagem + 1
elif p4 != 'NAO':
    print('Recarregue o programa e digite SIM ou NAO apenas!'), quit()
p5 = input('Já trabalhou com a vítima? ')
if p5 == 'SIM':
    contagem = contagem + 1
elif p5 != 'NAO':
    print('Recarregue o programa e digite SIM ou NAO apenas!'), quit()

if contagem == 2:
    print('Classificada como suspeita!')
elif contagem == 3 or contagem == 4:
    print('Classificada como Cúmplice')
elif contagem == 5:
    print('Classificada como Assasino!')
else:
    print('classificado como Inocente!')
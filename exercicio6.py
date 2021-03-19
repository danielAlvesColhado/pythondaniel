#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                     Até 5 Kg           Acima de 5 Kg
#
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

quantidade_macas = float(input('Qual a quantidade de maçãs em Kg? '))
quantidade_morango = float(input('Qual a quantidade de morangos em Kg? '))

if quantidade_morango <= 5:
    morango = 2.50
else: morango = 2.20

if quantidade_macas <= 5:
    maca = 1.80
else: maca = 1.50

quantidade_total = quantidade_morango + quantidade_macas
valor_total = maca * quantidade_macas + morango * quantidade_morango

print(f'o preço por Kg de maça é R$ {maca} e o preço por Kg de morango é R$ {morango}')
if quantidade_total > 8 or valor_total > 25:
    valor_total = valor_total * 0.90
    print(f'Voce ganhou R$ {valor_total * 0.10:.2f} de desconto!')
print(f'Valor total por {quantidade_morango}Kg de morango mais {quantidade_macas}kg de maça é R$ {valor_total:.2f}')
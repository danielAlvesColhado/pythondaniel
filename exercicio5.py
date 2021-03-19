#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
#o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

G = float(2.50)
A = float(1.90)
tipo = input('Qual tipo de combustível? digite A-alcool ou G-gasolina  ')
quantidade_vendida = float(input('qual a quantidade em Litros?  '))

if tipo.upper() == 'A':
    tipo = 'Alcool'
    if quantidade_vendida <= 20:
        A = A * 0.97
        total = A * quantidade_vendida
    elif quantidade_vendida > 20:
        A = A * 0.95
elif tipo.upper() == 'G':
    tipo = 'Gasolina'
    if quantidade_vendida <= 20:
        G = G * 0.96
        total = G * quantidade_vendida
    elif quantidade_vendida > 20:
        G = G * 0.94
        total = G * quantidade_vendida

print(f'com o desconto ja calculado você pagara R${total:.2f} por {quantidade_vendida}L de {tipo}')

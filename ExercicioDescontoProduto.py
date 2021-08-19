#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float(input('Digite o valor do produto R$'))
dsc = produto - (produto*5/100)

print('O valor com 5% de desconto é R${:.2f}'.format(dsc))
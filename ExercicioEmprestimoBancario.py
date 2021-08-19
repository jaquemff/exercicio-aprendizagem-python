#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

from time import sleep

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário do comprador: '))
ano = float(input('Digite em quantos anos será pago: '))

prestacao = valor_casa/(ano*12)
print('PROCESSANDO...')
sleep(1)

if prestacao > (salario*30)/100:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO ACEITO!')
    print('O valor da prestação ficou em R${:.2f} e será pago em {} anos.'.format(prestacao, ano))
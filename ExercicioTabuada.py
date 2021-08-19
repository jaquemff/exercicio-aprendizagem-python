#Faça a tabuada de um determinado número utilizando o laço 'for'

n = int(input('Digite um número inteiro: '))

for i in range(0, 11):
    print('{} x {} = {}'.format(n, i, n*i))

'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado
for negativo'''
cont = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    else:
        for cont in range(1, 11):
            print('{} x {} == {}'.format(n, cont, (n*cont)))
print('PROGRAMA ENCERRADO!')
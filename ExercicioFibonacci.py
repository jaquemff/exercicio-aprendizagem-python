'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma sequência de Fibonacci'''

termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3

print('{} - {}'.format(t1, t2), end='')

while cont <= termo:
    t3 = t1 + t2
    print(' - {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('- FIM')
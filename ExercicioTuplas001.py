'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e
20) e mostrá-lo por extenso'''

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n2 = int(input('Digite um valor entre 0 e 10: '))
    if 0 <= n2 <=10:
        break
        print('Tente novamente. ', end='')
print('O número digitado foi {}.'.format(n[n2]))

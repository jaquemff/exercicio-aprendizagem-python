'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''

#MANEIRA 1 DE REALIZAR O EXERCÍCIO
import math
n = int(input('Digite um número para calcular seu fatorial: '))
n1 = math.factorial(n)
print('O fatorial de {} é {}.'.format(n, n1))

#MANEIRA 2 DE REALIZAR O EXERCÍCIO
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
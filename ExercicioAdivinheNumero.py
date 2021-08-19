#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5.
#Peça para o usuário descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

n = int(input('Digite um número inteiro entre 0 e 5: '))
n2 = random.randint(0, 5)

print('PROCESSANDO...')
sleep(2)

if n==n2:
    print('Você VENCEU!')
else:
    print('Você PERDEU!')

print('O valor sorteado foi {}.'.format(n2))

#Melhore o jogo de adivinhar o número, onde o computador vai pensar em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

import random

n1 = -1
contador = 0
n2 = random.randint(0, 10)

while n1 != n2:
    n1 = int(input('Digite um número entre 0 e 10: '))
    contador += 1

    if n1 == n2:
        print('Você ACERTOU!')
print('Você acertou após {} palpites.'.format(contador))
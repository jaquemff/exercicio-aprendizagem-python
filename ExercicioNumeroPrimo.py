#Faça um programa que leia um número inteiro e diga quantas vezes ele foi dividido - utilizar cores

n = int(input('Digite um número: '))
tot = 0
for i in range(1, n + 1):
    if n%i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
#podem ou não formar um triângulo

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('PODEM formar um triângulo!')
else:
    print('NÃO podem formar um triângulo!')
'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre: quantas vezes apareceu o valor 9, em que posição foi digitada o
primeiro valor 3, quais foram os números pares'''

num = int(input('Digite um valor: ')),\
    int(input('Digite um valor: ')),\
    int(input('Digite um valor: ')),\
    int(input('Digite um valor: '))

print('O número 9 apareceu: {} vezes.'.format(num.count(9)))
if 3 in num:
    print('A posição do primeiro número 3 foi: {}° posição.'.format(num.index(3)+1))
else:
    print('O número 3 não foi encontrado em nenhuma posição!')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

#Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra 'a'
# - Em que posição ela aparece a priemira vez
# - Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()

if (frase.count('A') > 0):
    print('A letra a aparece {} vezes.'.format(frase.count('A')))
    print('A primeira posição de a é {}.'.format(frase.find('A')))
    print('A última posição de a é {}.'.format(frase.rfind('A')))
else:
    print('Não há letras "A" na frase digitada.')